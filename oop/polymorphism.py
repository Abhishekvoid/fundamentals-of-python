

# polymorphism

"""

- Polymorphism is that allow objects of different class to be treated the same. it shifts the focus from data types to behaviors.

- enables you to use single interface to represent different underlying classes. in python, polymorphism is achived primarily through duck typing, but you can also implement it through inheritance and method overriding.

- enchances flexibility and maintainability by allowing you to write more generic and resuable code.
"""

class Duck:
    def swim(self):
        print("The duck is swimming.")

class Albatross:
    def swim(self):
        print("The albatross is swimming.")


birds = [Duck(), Albatross()]

for bird in birds:
    bird.swim()



# inheritance + overriding methods
# using base class and override a method in subclasses

class Animal():
    def speak(self):
        print("Animals speaks")
    
class Dog(Animal):                           # animal is baseclass
    def speak(self):                         # overriding method in subclass   
        print("woof, woof")

class Cat(Animal):
    def speak(self):
        print("meow, meow")

def make_animal_speak(animal):
    animal.speak()


dog = Dog()
cat = Cat()

make_animal_speak(dog)
make_animal_speak(cat)

# 2. example

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        ...
    

class Rectangle(Shape):
    def __init__(self, width: float, height:float):
        self.width = width
        self.height = height
    
    def area(self)-> float:
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return (3.14* self.radius*self.radius)
    
def total_area(shapes: Shape) -> float:

    
    return sum(s.area() for s in shapes)

shapes = [Rectangle(9,4), Circle(2)]
print(total_area(shapes))

