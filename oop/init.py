

# __init__ is a intializer, intialize the object

class HMI:

    def __init__(self, no_tag, power):

        self.no_tag = no_tag
        self.power = power
    

exor = HMI("exortect67")


# multiple parameters in __init__

class Location:

    def __init__(self, name, lon, lat):
        self.name = name
        self.lon = lon
        self.lat = lat


loc = Location("warehouse", 64.34354, 12.343256)

"""

same arguments rules apply:
    - postional first
    - keyword after
"""

# adding default values in __init___

class User:

    def __init__(self, username, role="user"):

        self.username = username
        self.role = role


# mutable default arguments

class User:

    def __init__(self, tags = []):

        self.tags = tags

# why bad
#   - shared across instance

class User:

    def __init__(self, tags=None):

        self.tags = tags if tags else []
    

# 9. Constructor logic: what is allowed

"""
Allowed:
    - Assign attribute
    - Light validation
    - depency injection

Avoid:
    - DB calls
    - Network calls
    - Heavy computation

why?
    object creation should be cheap and predictable
"""

# Production Example

class UserService:

    def __init__(self, repo, validator):

        self.repo = repo
        self.validator = validator


# inheritance + __init__

class hot_drink:
    def __init__(self, coffee):
        self.coffee = coffee    

class bevrages(hot_drink):

    def __init__(self, coffee, shake):
        super().__init__(coffee)
        self.shake = shake
        