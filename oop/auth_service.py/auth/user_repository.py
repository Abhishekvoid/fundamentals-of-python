
from .user import User

class UserRepository:
    def __init__(self):
        self._users_by_email = {}

    def save(self, user: User):
        self._users_by_email[user.email] = user
        return user

    def find_by_email(self, email: str):
        return self._users_by_email.get(email)
