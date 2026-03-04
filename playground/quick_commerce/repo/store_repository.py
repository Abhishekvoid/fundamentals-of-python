from typing import Dict, Optional
from models.quick_commerce import Store

class StoreRepository:
    def __init__(self):
        self._stores = {
            "store_001": Store(
                store_id="store_001",
                name="Zepto Mart - Andheri",
                store_lat=19.1164, 
                store_lng=72.8379,
                is_closed=False,
                max_orders_per_hour=150
            ),
            "store_002": Store(
                store_id="store_002", 
                name="Blinkit Superstore - Bandra",
                store_lat=19.0664,
                store_lng=72.8277,
                is_closed=False,
                max_orders_per_hour=120
            )
        }
    
    async def get(self, store_id: str) -> Optional[Store]:
        return self._stores.get(store_id)