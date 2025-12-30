
# 1. Why oop exist

"""
Problems:
    - No shared state
    - Hard to group logic
    - Hard to scale
    - No "identity"

OOP solves this by binding data + behavior together 
"""


# 2. Class and Objects

"""

2.1. class
    - class is a blueprint
    An object is an instance
"""

# class
class user:  
    pass

# object
u = user()

# under the hood
u = user.__call__()

"""
Python:
    - allocates memory
    - creates an empty object
    - returns it
"""


# 2.2. __init__ (constructor)

class user:
    def __init__(self, username, email): # self means object itself
        self.username =  username
        self.email = email

# usage:

u = user("abhi", "a@gmail.com")

# 2.3. instance variable and class variables

class user:
    role = "user"   # class variable also the shared variable

    def __init__(self, username):
        self.username = username    # instance variable also the unique variable

u1 = user("fish")
u2 = user("cat")

