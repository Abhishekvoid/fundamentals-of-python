from typing import List, Optional, Dict
from models.quick_commerce import Order, OrderStatus
from repo.base import BaseRepository
import uuid

class OrderRepository(BaseRepository):
    def __init__(self):
        self._orders: Dict[str, Order] = {}
        self._order_id_index: Dict[str, str] = {}  # order_id → uuid
    
    async def save(self, order: Order) -> Order:
        self._orders[str(order.id)] = order
        self._order_id_index[order.order_id] = str(order.id)
        return order
    
    async def get(self, id: str) -> Optional[Order]:
        return self._orders.get(id)
    
    async def get_by_order_id(self, order_id: str) -> Optional[Order]:
        uuid_key = self._order_id_index.get(order_id)
        return self._orders.get(uuid_key) if uuid_key else None
    
    async def list(self, filters: Optional[Dict] = None) -> List[Order]:
        all_orders = list(self._orders.values())
        if not filters:
            return all_orders
        
        filtered = []
        for order in all_orders:
            if filters.get('status') and order.status != filters['status']:
                continue
            if filters.get('store_id') and order.store_id != filters['store_id']:
                continue
            filtered.append(order)
        return filtered
    
    async def delete(self, id: str) -> bool:
        if id in self._orders:
            del self._orders[id]
            return True
        return False