import uuid

class User:
    def __init__(self, username, email, password_hash, role="user", is_verified=False):
        self.__id = uuid.uuid4()
        self.__username = username
        self.__email = email
        self.__password_hash = password_hash
        self.__role = role
        self.__is_verified = is_verified

    @property
    def id(self):
        return self.__id
    
    @property
    def username(self):
        return self.__username
    
    @property
    def email(self):
        return self.__email

    @property
    def is_verified(self):
        return self.__is_verified
    
    @property
    def password_hash(self):
        return self.__password_hash

    def mark_verified(self):
        self.__is_verified = True
