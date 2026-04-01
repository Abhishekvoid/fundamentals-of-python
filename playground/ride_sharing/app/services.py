from typing import Optional, List
import math  

class RideMatchingService:
    def __init__(self, drivers: List[Driver]):
        self.drivers = [d for d in drivers if d.is_available]

    def calculate_distance(self, loc1: Location, loc2: Location) -> float:
        # Haversine formula (km)
        R = 6371
        dlat = math.radians(loc2.lat - loc1.lat)
        dlon = math.radians(loc2.lng - loc1.lng)
        a = (math.sin(dlat/2)**2 + math.cos(math.radians(loc1.lat)) *
             math.cos(math.radians(loc2.lat)) * math.sin(dlon/2)**2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        return R * c

    def estimate_fare(self, request: RideRequest, vehicle_type: VehicleType) -> float:
        distance = self.calculate_distance(request.pickup, request.dropoff)
        base_fare = {"bike": 20, "auto": 40, "car": 60}[vehicle_type]
        return base_fare + (distance * 10)  # Simple pricing

    def find_nearest_driver(self, request: RideRequest, max_distance_km: float = 5.0) -> Optional[Driver]:
        best_driver: Optional[Driver] = None
        min_dist = float('inf')
        for driver in self.drivers:
            if driver.vehicle_type != request.vehicle_type:
                continue
            if driver.current_location:
                dist = self.calculate_distance(request.pickup, driver.current_location)
                if dist < min_dist and dist <= max_distance_km:
                    min_dist = dist
                    best_driver = driver
        return best_driver

    def create_ride(self, request: RideRequest) -> Ride:
        driver = self.find_nearest_driver(request)
        fare = self.estimate_fare(request, request.vehicle_type)
        return Ride(
            id="ride_123",
            request=request,
            driver=driver,
            fare_estimate=fare
        )