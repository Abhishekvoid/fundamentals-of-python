
from abc import ABC, abstractmethod
class Location(ABC):
    @abstractmethod
    def move(self, robo_id: int, lang: float, lat: float, message: str) -> None:
        ...

class MuleLocation(Location):

    def move(self,  robo_id: int, lang: float, lat: float,  message: str) -> None:
        print(f"{robo_id} Mule moved to longitute: {lang} and latitutde: {lat} and {message}")

class DroneLocation(Location):

    def move(self,  robo_id: int, lang: float, lat: float, message: str):
        print(f"{robo_id} Drone moved to longitute: {lang} and latitutde: {lat}, {message}")

class Boston_Atlas(Location):

    def move(self,  robo_id: int, lang: float, lat: float, message: str):
        print(f"{robo_id} Atlas moved to longitute: {lang} and latitutde: {lat}, {message}")
    

def Robot_movements(robots: list[Location], robo_id: int, lang: float, lat: float, message: str):
    for robot in robots:
        robot.move(robo_id, lang, lat, message)

robot_location = [

    MuleLocation(),
    DroneLocation(),
    Boston_Atlas()
]

Robot_movements(robot_location, 677, 45.3454365, 12.5465467547, "weroufbweru")



# different argument to each class
class Robot_movements1:
    def __init__ (self, movement: tuple[Location, float, float]):
    
        self._movement =  movement
    
    def moves(self, robo_id: int) -> None:

        for methods, lang, lat in self._movement:
            methods.move(robo_id, lang, lat, "hello")

robot_location = [

    (MuleLocation(), 23.43235, 12.32454325),
    (DroneLocation(), 56.64574, 19.534543),
    (Boston_Atlas(), 33.453456, 13.4335)
]

save = Robot_movements1(robot_location)
save.moves(robo_id=47)


mule_robot = MuleLocation()
mule_robot.move(1, 23.43235, 12.32454325, "Mule Robot locating")

drone_robot = DroneLocation()
drone_robot.move(2, 43.53456, 11.34234, "Drone is moving")

atlas_robot = Boston_Atlas()
atlas_robot.move(3, 67.43423, 45.5365436, "Atlas spotted")
