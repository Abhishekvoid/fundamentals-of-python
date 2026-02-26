# test_client.py
import asyncio
from models import Container, YardZone, YardZoneType
from service import YardManagementService

async def main():
    service = YardManagementService()
    
    # Create zone
    zone = YardZone(
        zone_code="A1",
        zone_type=YardZoneType.IMPORT,
        capacity=100,
        current_load=0,
        total_slots=120
    )
    
    # Create container (BIC validated)
    container = await service.create_container(
        container_number="ABCU1234567",
        shipping_line="Maersk",
        yard_zone="A1",
        row="A12",
        stack_level=3
    )
    
    print(container)

asyncio.run(main())
