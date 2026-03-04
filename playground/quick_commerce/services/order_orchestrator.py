from typing import List, Optional
from datetime import datetime, timezone, timedelta
import uuid
import math
from models.quick_commerce import (
    Order, OrderItem, OrderStatus, RiderStatus, Rider
)
from repo import Order_Repository, StoreRepository, RiderRepository

class OrderOrchestrator:
    def __init__(self):
        self.order_repo = OrderRepository()
        self.store_repo = StoreRepository()
        self.rider_repo = RiderRepository()
    
    async def place_order(
        self, 
        customer_id: str,
        store_id: str,
        items: List[OrderItem],
        customer_lat: float,
        customer_lng: float,
        priority: str = "normal"
    ) -> Order:
        # 1. Validate store availability
        store = await self.store_repo.get(store_id)
        if not store or store.is_closed:
            raise ValueError(f"Store {store_id} unavailable")
        
        # 2. Calculate total + dynamic ETA
        total_amount = sum(item.price * item.quantity for item in items)
        base_distance_km = self._haversine(
            customer_lat, customer_lng, 
            store.store_lat, store.store_lng
        )
        
        # Priority ETA: Express=8min, Normal=15min base
        eta_minutes = 8 if priority == "express" else 15
        eta_minutes += int(base_distance_km * 2)  # 2min/km
        
        order = Order(
            order_id=f"ORD-{datetime.now().strftime('%Y%m%d')}-{str(uuid.uuid4())[:4].upper()}",
            customer_id=customer_id,
            customer_lat=customer_lat,
            customer_lng=customer_lng,
            store_id=store_id,
            store_lat=store.store_lat,
            store_lng=store.store_lng,
            items=items,
            total_amount=total_amount,
            priority=priority,
            eta_minutes=max(eta_minutes, 10),  # Min 10min SLA
            status=OrderStatus.PLACED
        )
        
        # 3. Save + auto-assign rider
        saved_order = await self.order_repo.save(order)
        rider = await self._assign_rider(saved_order)
        if rider:
            saved_order.assigned_rider = rider.rider_id
            await self.order_repo.save(saved_order)
        
        return saved_order
    
    async def _assign_rider(self, order: Order) -> Optional[Rider]:
        # Rider matching engine (Zepto's $100M algorithm)
        riders = await self.rider_repo.list_nearby(
            order.customer_lat, order.customer_lng, radius_km=3.0
        )
        
        best_rider = None
        best_score = float('inf')
        
        order_weight = sum(item.quantity * 0.5 for item in order.items)  # 500g/item
        
        for rider in riders:
            if rider.status != RiderStatus.IDLE:
                continue
                
            if order_weight > rider.max_weight:
                continue
            
            # Distance score (primary)
            distance_km = self._haversine(
                rider.current_lat, rider.current_lng,
                order.customer_lat, order.customer_lng
            )
            
            # Priority bonus for Express
            priority_bonus = -2.0 if order.priority == "express" else 0
            
            score = distance_km + priority_bonus
            
            if score < best_score:
                best_score = score
                best_rider = rider
        
        if best_rider:
            best_rider.status = RiderStatus.BUSY
            await self.rider_repo.save(best_rider)
        
        return best_rider
    
    async def update_order_status(
        self, 
        order_id: str, 
        new_status: OrderStatus
    ) -> Order:
        order = await self.order_repo.get_by_order_id(order_id)
        if not order:
            raise ValueError(f"Order {order_id} not found")
        
        order.status = new_status
        order.last_updated = datetime.now(timezone.utc)
        
        # Auto-progression logic
        if new_status == OrderStatus.PICKED:
            order.status = OrderStatus.PACKED
        elif new_status == OrderStatus.PACKED:
            order.status = OrderStatus.OUT_DELIVERY
        
        return await self.order_repo.save(order)
    
    def _haversine(self, lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """Haversine distance in km"""
        R = 6371  # Earth radius
        
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.asin(math.sqrt(a))
        
        return R * c