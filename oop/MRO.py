

# MRO method resoluation order

"""
- MRO is the order follow by python in order to follows the look up attributes and methods in a class hierarchy, it determines which methods or attribute to use when names collide in multiple inheritance scenarios
"""

class A:
    def speak(self):
        return "A"

class B: 
    def speak(self):
        return "B"
    
class C(A):
    def speak(self):
        return "C"

class D(B, C):
    pass

print(D.__mro__)


class Base:
    def __init__(self):
        print("Base")
        super().__init__()

class PaymentLogging(Base):
    def __init__(self):
        print("paymentLoggging")
        super().__init__()

class FraudCheck(Base):
    def __init__(self):
        print("FraudCheck")
        super().__init__()

class AdvancePaymentService(FraudCheck, PaymentLogging):
    def __init__(self):
        print("AdvancePayment")
        super().__init__()

AdvancePaymentService()
print(AdvancePaymentService.__mro__)