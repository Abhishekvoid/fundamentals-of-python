"""
Service Layer (Composition)

Problem:

- Create:
    - Validator class
    - Repository class
    - UserService class

- UserService must:

    - use validator
    - use repository
    - not inherit from them

Goal:
Show HAS-A relationship
"""


class Validator():

    def validate(self, data:dict) -> tuple[bool, str | None]:

        if not data.get("username"):
            return False, "username required"      

        if "@" not in data.get("email", ""):
            return False, "Emial is invalid" 

        if len(data.get("password", "")) < 8 :
            return False, "password is not strong"

        return True, "user is valid"
class Repository():

    def save(self, data: dict) -> None:

        print(f"saving user to database...")
        print(f"username: {data["username"]} and email is: {data["email"]}")


class UserService():

    def __init__(self, validator: Validator, repo: Repository):

        self.validator = validator
        self.repo = repo

    def register(self, data: dict) -> None:

        is_valid, message = self.validator.validate(data)
        if not is_valid:
            print("validation failed", message)
        if self.validator.validate(data):
            self.repo.save(data)

validator = Validator()
repo = Repository()
service = UserService(validator, repo)

service.register({

    "username": "john",
    "email": "john@example.com",
    "password": "superpass"
})