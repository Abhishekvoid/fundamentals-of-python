from passlib.hash import bcrypt

class PasswordHasher:
    def hash(self, raw_password: str) -> str:
        return bcrypt.hash(raw_password)

    def verify(self, raw_password: str, password_hash: str) -> bool:
        return bcrypt.verify(raw_password, password_hash)
