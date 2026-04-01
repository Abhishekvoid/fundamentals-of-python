from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from .models import RideRequest, Ride, Driver, Location, VehicleType
from .services import RideMatchingService

router = APIRouter(prefix="/api/v1", tags=["rides"])

# Mock drivers
SAMPLE_DRIVERS = [
    Driver(id="d1", user=User(id="u1", name="Driver Raj", role="driver", phone="+91-1234", rating=4.8), 
           vehicle_type="bike", vehicle_number="GJ01AB1234", is_available=True,
           current_location=Location(lat=23.0225, lng=72.5714)),
    Driver(id="d2", user=User(id="u2", name="Auto Sharma", role="driver", phone="+91-5678", rating=4.5),
           vehicle_type="auto", vehicle_number="GJ01XX9999", is_available=True,
           current_location=Location(lat=23.0250, lng=72.5700))
]

service = RideMatchingService(SAMPLE_DRIVERS)

@router.post("/rides", response_model=Ride)
async def create_ride(request: RideRequest):
    ride = service.create_ride(request)
    return ride

@router.get("/rides/{ride_id}", response_model=Ride)
async def get_ride(ride_id: str):
    # Simulate DB fetch
    raise HTTPException(404, "Ride not found")  # Extend with real storage

@router.get("/drivers", response_model=List[Driver])
async def list_drivers():
    return service.drivers