import jwt
import datetime

class TokenService:
    def __init__(self, secret_key: str, access_ttl_minutes: int = 15):
        self.secret_key = secret_key
        self.access_ttl = access_ttl_minutes

    def create_access_token(self, user):
        payload = {
            "sub": str(user.id),
            "email": user.email,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=self.access_ttl),
        }
        return jwt.encode(payload, self.secret_key, algorithm="HS256")

    def verify_access_token(self, token: str):
        try:
            return jwt.decode(token, self.secret_key, algorithms=["HS256"])
        except Exception:
            return None
