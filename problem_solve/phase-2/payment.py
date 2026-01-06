"""
Problem:

- Create a base class Payment
- Subclasses:

    - UPI
    - Card

- Each implements pay()
- Write a function checkout(payment)
Goal:
Demonstrate polymorphism

"""

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, user_id:int, amount:int, ) -> None:
        ...

class UPIPayment(Payment):
    def pay(self, user_id: int, amount:int) -> None:
        print(f"payment of: {amount} via UPI, user: {user_id}")

class CardPayment(Payment):
    def pay(self, user_id: int, amount:int) -> None:
        print(f"payment of: {amount} via Card, user: {user_id}")

class CashPayment(Payment):
    def pay(self, user_id: int, amount:int) -> None:
        print(f"payment of: {amount} via Cash, user: {user_id}")

class PaymentService:
    def __init__(self, payments: list[Payment]):
        self._payment = list(payments)
    

    def billing(self, user_Id: int, amount: int) -> None:
        for payment in self._payment:
            payment.pay(user_Id, amount )

payments = [UPIPayment(), CardPayment(), CashPayment()]
billing_pay = PaymentService(payments)

billing_pay.billing(43, 566)