from typing import List
from models.quick_commerce import Rider, RiderStatus
from repo.base import BaseRepository
import math
from typing import Tuple

class RiderRepository(BaseRepository):
    def __init__(self):
        self._riders: Dict[str, Rider] = {}
    
    async def save(self, rider: Rider) -> Rider:
        self._riders[rider.rider_id] = rider
        return rider
    
    async def get(self, rider_id: str) -> Rider:
        return self._riders.get(rider_id)
    
    async def list(self, filters: Optional[Dict] = None) -> List[Rider]:
        return list(self._riders.values())
    
    async def list_nearby(
        self, 
        lat: float, 
        lng: float, 
        radius_km: float = 3.0
    ) -> List[Rider]:
        nearby = []
        for rider in self._riders.values():
            if rider.status != RiderStatus.IDLE:
                continue
            distance = self._haversine(lat, lng, rider.current_lat, rider.current_lng)
            if distance <= radius_km:
                nearby.append(rider)
        return nearby
    
    def _haversine(self, lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        R = 6371
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.asin(math.sqrt(a))
        return R * c
    
    async def delete(self, rider_id: str) -> bool:
        if rider_id in self._riders:
            del self._riders[rider_id]
            return True
        return False