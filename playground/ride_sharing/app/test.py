import pytest
from app.models import RideRequest, Location, VehicleType
from app.services import RideMatchingService
from app.api import SAMPLE_DRIVERS

@pytest.fixture
def service():
    return RideMatchingService(SAMPLE_DRIVERS)

def test_create_ride_bike(service):
    request = RideRequest(
        rider_id="r1",
        pickup=Location(lat=23.0225, lng=72.5714),
        dropoff=Location(lat=23.0333, lng=72.5667),
        vehicle_type=VehicleType.BIKE
    )
    ride = service.create_ride(request)
    assert ride.driver is not None
    assert ride.fare_estimate > 20  # Base fare check

def test_no_driver_available(service):
    # Modify to unavailable
    service.drivers[0].is_available = False
    request = RideRequest(rider_id="r1", pickup=Location(0,0), dropoff=Location(0,1), vehicle_type=VehicleType.CAR)
    ride = service.create_ride(request)
    assert ride.driver is None