from .user import User

class AuthService:
    def __init__(self, user_repo, hasher, token_service):
        self.user_repo = user_repo
        self.hasher = hasher
        self.token_service = token_service

    def register(self, username, email, raw_password):
        existing = self.user_repo.find_by_email(email)
        if existing:
            raise ValueError("Email already exists")

        password_hash = self.hasher.hash(raw_password)
        user = User(username, email, password_hash)
        self.user_repo.save(user)
        return user

    def login(self, email, raw_password):
        user = self.user_repo.find_by_email(email)
        if not user:
            raise ValueError("Invalid credentials")
        
        if not self.hasher.verify(raw_password, user.password_hash):
            raise ValueError("Invalid credentials")

        if not user.is_verified:
            raise ValueError("Email not verified")

        return self.token_service.create_access_token(user)
