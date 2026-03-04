from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from models.quick_commerce import Order, Rider, Store

class BaseRepository(ABC):
    @abstractmethod
    async def save(self, entity: Any) -> Any:
        pass
    
    @abstractmethod
    async def get(self, id: str) -> Optional[Any]:
        pass
    
    @abstractmethod
    async def list(self, filters: Optional[Dict] = None) -> List[Any]:
        pass
    
    @abstractmethod
    async def delete(self, id: str) -> bool:
        pass