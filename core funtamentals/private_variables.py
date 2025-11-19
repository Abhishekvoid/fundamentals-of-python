
# What are Private Variables

"""

Private variables only accessible within the class they are defined in. this is done to protect data to ensure that it is not modified or accessed by unauthorized code snippets

# Public Variables:  can be accessible from anywhere both inside or or outside of the class and can be      accessed by anyone

# Protected Variables: can be accessible in the class or its subclass but not outsiders

"""

# Defining Private Variables in Python

class MyClass: 
    def __init__(self):
        self._private_var = "I am private"

    def show_private(self):
        return self._private_var

obj = MyClass()
print(obj.show_private())


# Private Methods in Python

"""
private methods only accessible to within in the class they are define in. 
"""

class MyClass:
    def __init__(self):
        self.__private_var = "I am private"
    
    def __private_method(self):
        return " This is a private method"
    
    def show_private(self):
        return self.__private_var + "and" + self.__private_method()

obj = MyClass()

print(obj.show_private())

print(obj._MyClass__private_method())


# Real World Example of Private Variables

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount
        return self.__balance
    
    def withdraw(self, amount):

        if 0 < amount <= self.__balance:
            self.__balance -= amount
        return self.__balance
    
    def get_balance(self):
        return self.__balance


account = BankAccount("12345", 1000)

try:
    account.__balance += 500
except AttributeError:
    print("Direct access to private variables failed!!!")



print("Your account balance is: ", account.get_balance())

account.deposit(500)
print("Your account balance after deposit is: ", account.get_balance())
    