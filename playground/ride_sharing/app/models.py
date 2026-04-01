from pydantic import BaseModel, Field, validator
from typing import List, Optional, Literal
from datetime import datetime
from enum import Enum

class UserRole(str, Enum):
    RIDER = "rider"
    DRIVER = "driver"

class VehicleType(str, Enum):
    BIKE = "bike" 
    AUTO = "auto"
    CAR = "car"  

class Location(BaseModel):
    lat: float = Field(..., ge=-90, le=90)
    lng: float = Field(..., ge=-180, le=180)

class User(BaseModel):
    id: str
    name: str
    role: UserRole
    phone: str
    rating: float = Field(0.0, ge=0.0, le=5.0)

class Driver(BaseModel):
    id: str
    user: User
    vehicle_type: VehicleType
    vehicle_number: str
    is_available: bool = True
    current_location: Optional[Location] = None

class RideRequest(BaseModel):
    rider_id: str
    pickup: Location
    dropoff: Location
    vehicle_type: VehicleType = VehicleType.BIKE
    eta_minutes: Optional[int] = None  # Estimated time

    @validator('pickup', 'dropoff')
    def valid_coords(cls, v):
        if abs(v.lat) > 90 or abs(v.lng) > 180:
            raise ValueError('Invalid coordinates')
        return v

class Ride(BaseModel):
    id: str
    request: RideRequest
    driver: Optional[Driver] = None
    status: Literal["requested", "accepted", "ongoing", "completed", "cancelled"] = "requested"
    fare_estimate: Optional[float] = None
    created_at: datetime = Field(default_factory=datetime.now)