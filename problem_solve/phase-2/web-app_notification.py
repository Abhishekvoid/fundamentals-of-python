from abc import ABC, abstractmethod

# base class
"""
parent class notifier with send method
"""

class Notifier(ABC):
    @abstractmethod
    def send(self, user_id: int, message: str) -> None:
        ...

class EmailNotifier(Notifier):
    def send(self, user_id:int, message:str) -> None:
        print(f"Email to: {user_id} message is: {message}")

class SmsNotifier(Notifier):
    def send(self, user_id:int, message:str) -> None:
        print(f"Sms to: {user_id} message is: {message}")

class PusNotifier(Notifier):
    def send(self, user_id:int, message:str) -> None:
        print(f"Push to: {user_id} message is: {message}")

class NotificationService:
    def __init__(self, notifiers = list[Notifier]):
        self._notifiers = notifiers
    

    def send_Welcome(self, user_id: int) -> None:
        for notifier in self._notifiers:
            notifier.send(user_id, "welcome to the app!")

notifiers = [EmailNotifier(),SmsNotifier(), PusNotifier()]
service = NotificationService(notifiers)

service.send_Welcome(42)