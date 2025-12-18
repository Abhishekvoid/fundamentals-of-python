
class Car:

    def __init__(self, brand, model, price):

        self.brand =brand
        self.model = model
        self.price =  price

    def inIndia(self):
            return (f"following car is {self.brand}, {self.model} at price of: {self.price}")


class Engine:
     
    def __init__(self, power, torque, type):
         
        self.power = power
        self.torque = torque
        self.type = type
     
class ElectricCar(Car):
     
    def __init__(self, brand, model, price, batterySize, engine: Engine ):
         super().__init__(brand, model, price)
         self.batterSize = batterySize
         self.engine = engine
    
my_car = Car("Toyota", "Supra", 26348394)
print(f"{my_car.brand}, {my_car.model} price is: {my_car.price}")
print(my_car.inIndia())       




my_engine = Engine(500, 600, "electric")
tesla = ElectricCar("Tesla", "Model S", 100000, 120, my_engine)
print(f"{tesla.brand}, {tesla.model} price is: {tesla.price} with battery size of: {tesla.batterSize } engine is: {tesla.engine.power}")


a = 100
b = a

print(f"id of a: {id(a)}, id of b: {id(b)}")  

b += 1

print(f"id of a: {id(a)}, id of b after change: {id(b)}")  