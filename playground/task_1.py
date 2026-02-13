
# Difficulty: Easy (OOP Basics) Time Limit: 10 Minutes

    # Scenario: You are writing the firmware for a warehouse robot. You need to create a class LogisticsRobot that tracks the robot's battery life and movement status.

# Requirements:

# 1. Initialize (__init__):

#   The robot must accept a name (string) when created.
#   It should always start with battery_level at 100.
#   It should always start with location at 0 (position on a 1D line).

#2. Method move(steps):

#   Takes an integer steps (distance to move).
#   Moving costs 5% battery per step.

# Logic:

#   Check if the robot has enough battery to make the full move.

#    If YES: Update the location (add steps), decrease the battery_level, and print "[Name] moved to location [X]".

#   If NO: Do not move. Print "[Name] does not have enough battery!".

#3. Method charge():

#   Reset battery_level to 100.
#   Print "[Name] is recharging... Battery full.".

# 4.  Method status():

#   Print the current state: "[Name] | Battery: [X]% | Location: [Y]".



class LogisticsRobot:
    def __init__(self, name, battery_level=100, location = 0):

        self.name = name
        self.battery = battery_level
        self.location = location
    

    def move(self, steps):

        cost = (steps * 5)
        if self.battery < cost:
            print(f"{self.name} does not have enough battery! (Cost: {cost}, have: {self.battery})")
            return

       
        self.location += steps          
        self.battery -= cost           

        print(f"{self.name} moved to location {self.location} (Cost: {cost} battery)")
    
        
    def charge(self):
        self.battery = 100
        print(f"{self.name} is recharging... battery is full.")
    

    def status(self):
        print(f"{self.name} | {self.battery} | {self.location}")
            
    
bot = LogisticsRobot("Speedy-1")
bot.status()          # Expected: Battery: 100% | Location: 0

bot.move(4)           # Expected: Moved to location 4 (Cost: 20 battery)
bot.status()          # Expected: Battery: 80% | Location: 4

bot.move(20)          # Expected: Not enough battery! (Cost: 100, have: 80)
bot.charge()          # Expected: Recharging...
bot.status()


class Drone(LogisticsRobot):

    def move(self, steps):

        
        cost = (steps*10)
        

        if self.battery < cost:
            print(f"{self.name} does not have enough battery! (Cost: {cost}, have: {self.battery}) || steps: {steps} || cost: {cost}")
            return
        self.location += steps
        self.battery -= cost

    def scan_area(self):
        print(f"{self.name} is scanning the warehouse from the air...")
        self.battery -= 5
        print(f"{self.battery}")

my_drone = Drone("Sky-Bot-1") 

my_drone.status()      # Expected: Battery 100 | Location 0
my_drone.move(3)       # Expected: "flew to..." (Cost 30 battery)
my_drone.scan_area()   # Expected: "scanning..." (Battery now 65)
my_drone.status()      # Expected: Battery 65 | Location 3

