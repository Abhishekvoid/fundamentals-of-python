
class Robot:

    def __init__(self, speed, location):
        self.speed = speed
        self.location = location
    
class MuleRobot(Robot):

    def __init__(self, speed, location, type):
        self.speed = speed
        self.location = location
        self.type = type

"""
this is called code duplication... even we are inherit the base class robot, we still re-declaring speed and location
    - time comsuming
    - performance and memory lose
"""


    
class MuleRobot(Robot):

    def __init__(self, speed, location, type):
        Robot.__init__(speed, location)
        self.type = type

"""
- this is explicit calling of the base function direct your subclass method, this is better than code duplication
but the more better way ->
"""


    
class MuleRobot(Robot):

    def __init__(self, speed, location, type):
        super().__init__(speed, location)
        self.type = type


"""
# super()
    - using super allow you to direct use method and base class which is inherting to the subclass,
    here MuleRobot inherit the base class Robot so, super will redirect the Robot class
"""