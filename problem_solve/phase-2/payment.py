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


# passing different amount per method
#    - we will map over the amount and method by passing: tuples(payment_obj, amount)

class PaymentService:
    def __init__(self, payment_with_amount: tuple[Payment, int]):

        self._payment_with_amount = payment_with_amount
    
    def billing(self, user_id: int):

        for methods, amount in self._payment_with_amount:
            methods.pay(user_id, amount)

payments = [

    (UPIPayment(), 500),  
    (CardPayment(), 300),  
    (CashPayment(), 200), 
]

billing_pay2 = PaymentService(payments)
billing_pay2.billing(user_id=47)

# 3. if arguments differ in shapes
"""
If each method needs extra fields (e.g., UPI ID, card number)
    - Keep a common pay(self, user_id, amount, **kwargs) signature in Payment.
    - Each subclass Reads only the kwargs it cares about.
"""

class UPI_idPayment(Payment):
    def pay(self, user_id:int, amount:int, **kwargs) -> None:
        upi_id = kwargs["upi_id"]
        print(f"{amount} via UPI  {upi_id} for user {user_id}")

class Card_idPayment(Payment):
    def pay(self, user_id: int, amount:int, **kwargs) -> None:
        card_id_last4 = kwargs["last4"]
        print(f"{amount} via UPI  {card_id_last4} for user {user_id}")

class PaymentService:
    def checkout(payment: Payment, user_id: int, amount: int, **kwargs) -> None:
        payment.pay(user_id, amount, **kwargs)

payment_via_UPI = PaymentService.checkout(UPI_idPayment(), 47, 500, upi_id ="user@upi")
payment_via_Card = PaymentService.checkout(Card_idPayment(), 67, 800,  last4 = "4206")

