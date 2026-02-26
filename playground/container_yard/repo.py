from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
import json
from pathlib import Path
import asyncio
from models import Container, YardZone

class BaseRepository(ABC):
    @abstractmethod
    async def save(self, entity: Any) -> Any: ...
    @abstractmethod
    async def get(self, id: str) -> Optional[Any]: ...
    @abstractmethod
    async def delete(self, id: str) -> bool: ...
    @abstractmethod
    async def list(self, filters: Dict[str, Any] = None) -> List[Any]: ...

class ContainerRepository(BaseRepository):
    def __init__(self, storage_path: str = "data/containers.json"):
        self.storage_path = Path(storage_path)
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)
        self._containers: Dict[str, Container] = {}
        self._load()
    
    def _load(self):
        if self.storage_path.exists():
            with open(self.storage_path, 'r') as f:
                data = json.load(f)
                self._containers = {c['id']: Container(**c) for c in data}
    
    def _save(self):
        data = [c.model_dump() for c in self._containers.values()]
        with open(self.storage_path, 'w') as f:
            json.dump(data, f, default=str)
    
    async def save(self, container: Container) -> Container:
        self._containers[str(container.id)] = container
        self._save()
        return container
    
    async def get(self, id: str) -> Optional[Container]:
        return self._containers.get(id)
    
    async def delete(self, id: str) -> bool:
        if id in self._containers:
            del self._containers[id]
            self._save()
            return True
        return False
    
    async def list(self, filters: Dict[str, Any] = None) -> List[Container]:
        containers = list(self._containers.values())
        if filters:
            containers = [c for c in containers if self._matches_filter(c, filters)]
        return containers
    
    def _matches_filter(self, container: Container, filters: Dict[str, Any]) -> bool:
        for key, value in filters.items():
            if getattr(container, key, None) != value:
                return False
        return True

class YardZoneRepository(BaseRepository):
    # Similar implementation to ContainerRepository
    def __init__(self, storage_path: str = "data/zones.json"):
        self.storage_path = Path(storage_path)
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)
        self._zones: Dict[str, YardZone] = {}
        self._load()
    
    # ... implement similar methods
    pass
