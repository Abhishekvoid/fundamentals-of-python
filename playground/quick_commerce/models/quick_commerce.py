from pydantic import BaseModel, Field, ConfigDict, field_validator
from typing import List, Optional
from datetime import datetime, timezone
from uuid import UUID, uuid4
from enum import Enum
import re

class OrderStatus(str, Enum):
    PLACED = "placed"
    PICKED = "picked"
    PACKED = "packed"
    OUT_DELIVERY = "out_delivery"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

class RiderStatus(str, Enum):
    IDLE = "idle"
    BUSY = "busy"
    OFFLINE = "offline"

class OrderItem(BaseModel):
    product_id: str
    name: str
    quantity: int = Field(ge=1)
    price: float = Field(gt=0)

class Order(BaseModel):
    model_config = ConfigDict(from_attributes=True, extra='forbid')
    
    id: UUID = Field(default_factory=uuid4)
    order_id: str = Field(..., pattern=r'^ORD-\d{8}-[A-Z]{4}$')
    customer_id: str = Field(min_length=10)
    customer_lat: float = Field(ge=-90, le=90)
    customer_lng: float = Field(ge=-180, le=180)
    store_id: str
    store_lat: float = Field(ge=-90, le=90)
    store_lng: float = Field(ge=-180, le=180)
    items: List[OrderItem]
    total_amount: float = Field(gt=0)
    priority: Literal["express", "normal"] = "normal"
    eta_minutes: int = Field(ge=5, le=60)
    status: OrderStatus = OrderStatus.PLACED
    assigned_rider: Optional[str] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class Rider(BaseModel):
    model_config = ConfigDict(from_attributes=True, extra='forbid')
    
    rider_id: str
    name: str
    current_lat: float
    current_lng: float
    max_weight: float = Field(gt=0)  # kg
    status: RiderStatus = RiderStatus.IDLE
    last_updated: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class Store(BaseModel):
    model_config = ConfigDict(from_attributes=True, extra='forbid')
    
    store_id: str
    name: str
    store_lat: float = Field(ge=-90, le=90)
    store_lng: float = Field(ge=-180, le=180)
    is_closed: bool = False
    max_orders_per_hour: int = 100