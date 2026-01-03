
# Compositon HAS-A relationship
"""
    "Means this object HAS another object"
"""

class Database:
    def save(self, data):
        print("saving", data)

class UserService:

    def __init__(self):
        self.db = Database()

    def save_user(self, user):
        self.db.save(user)

# UserService has a database

"""

Why composition is preferred in production
    Inheritance problems:
        - deep hierarchies
        - Ripple effects
        - hard to change base classes
    Composition Benefits:
        - loosely coupled
        - easy to replace dependencies
        - eaiser testing 
"""

# real architecture

class Validator:
    def validate(self, data):
        return True

class repository:

    def save(self, data):
        print("saved")

class UserService:
    def __init__(self, validator, repo):
        self.validator = validator
        self.repo = repo

    def register(self, data):
        if self.validator.validate(data):
            self.repo.save(data)
    
