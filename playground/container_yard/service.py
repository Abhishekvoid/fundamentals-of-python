from typing import List, Optional
from models import Container, YardZone, ContainerStatus
from repo import ContainerRepository, YardZoneRepository

class YardManagementService:
    def __init__(self):
        self.container_repo = ContainerRepository()
        self.zone_repo = YardZoneRepository()
    
    async def create_container(
        self, 
        container_number: str,
        shipping_line: str,
        yard_zone: str,
        row: str,
        stack_level: int
    ) -> Container:
        # Validate zone exists and has capacity
        zone = await self.zone_repo.get(yard_zone)
        if not zone or zone.current_load >= zone.capacity:
            raise ValueError(f"No capacity in zone {yard_zone}")
        
        container = Container(
            container_number=container_number,
            shipping_line=shipping_line,
            yard_zone=yard_zone,
            row=row,
            stack_level=stack_level
        )
        
        saved = await self.container_repo.save(container)
        await self._update_zone_load(yard_zone, +1)
        return saved
    
    async def move_container(
        self, 
        container_id: str, 
        new_zone: str, 
        new_row: str, 
        new_stack: int
    ) -> Container:
        container = await self.container_repo.get(container_id)
        if not container:
            raise ValueError(f"Container {container_id} not found")
        
        old_zone = container.yard_zone
        
        # Update zone loads
        await self._update_zone_load(old_zone, -1)
        await self._update_zone_load(new_zone, +1)
        
        # Update container
        container.yard_zone = new_zone
        container.row = new_row
        container.stack_level = new_stack
        container.last_updated = datetime.now(timezone.utc)
        container.status = ContainerStatus.IN_YARD
        
        return await self.container_repo.save(container)
    
    async def _update_zone_load(self, zone_code: str, delta: int):
        zone = await self.zone_repo.get(zone_code)
        if zone:
            zone.current_load += delta
            await self.zone_repo.save(zone)
    
    async def get_containers_by_status(self, status: ContainerStatus) -> List[Container]:
        return await self.container_repo.list({'status': status})
    
    async def get_zone_utilization(self, zone_code: str) -> Dict[str, float]:
        zone = await self.zone_repo.get(zone_code)
        if not zone:
            return {'utilization': 0.0}
        return {
            'zone_code': zone_code,
            'utilization': zone.current_load / zone.capacity * 100
        }
