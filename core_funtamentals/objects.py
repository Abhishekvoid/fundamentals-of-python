"""

Python object:

object as an instance of class, each object contain data and methods to operate on that data
"""

# Creating an object

"""
When creating a object from a class, we used a special method called the constructor, define as __init__()
"""

class car:
    def __init__(self, model, price):
        self.model  = model
        self.price = price


Merc = car("AMG", 1000000)
print(Merc.model)
print(Merc.price)


# Accessing class members

"""
You can access both instance and variables and methods of the class using the object. Instance variables are unique to each object, while methods define the behavior of the objects
"""

class Car:

    def __init__(self, model):
        self.model = model

    def setPrice(self, price):
        self.price = price
    
    def getPrice(self):
        return self.price
    
Audi = Car("R8")
Audi.setPrice(1000000)
print(Audi.getPrice())


# Exmaple 2


class Car:
    vehicle = 'Car'

    def __init__(self, model, price):
        self.model = model
        self.price = price

plate = Car("R8", 100000)
BMW = Car("I8", 10000000)

print(Audi.model, Audi.price)
print(BMW.model, BMW.price)


