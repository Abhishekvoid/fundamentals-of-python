
class Car:

    def __init__(self, brand, model, price):

        self.brand =brand
        self.model = model
        self.price =  price

    def inIndia(self):
            return (f"following car is {self.brand}, {self.model} at price of: {self.price}")
    
my_car = Car("Toyota", "Supra", 26348394)
print(f"{my_car.brand}, {my_car.model} price is: {my_car.price}")
print(my_car.inIndia())         