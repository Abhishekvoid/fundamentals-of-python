
# inheritance (IS-A relatioship)
#   "Child IS A type of parent"    

class User:

    def role(self):

        return "user"

class Admin(User):
    def role(self):
        return "admin"

a = Admin()
print(a.role()) # admin

"""

a.role()
    1. Look in admin
    2. if not found -> look in User
    3. Then -> object

this lookup chains in MRO


# when inheritance is good

    - cleas IS-A relationship
    - shared interface
    - polymorphism needed
"""
# Example

class Payment:
    def pay(self):
        raise NotImplementedError

class UPI(Payment):
    def pay(self):
        print("payment via UPI")

class Card(Payment):
    def pay(self):
        print("payment via card")

def checkout(payment: Payment):
    payment.pay() 