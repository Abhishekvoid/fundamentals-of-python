from auth.password_hasher import PasswordHasher
from auth.user_repository import UserRepository
from auth.token_service import TokenService
from auth.auth_service import AuthService

repo = UserRepository()
hasher = PasswordHasher()
token_service = TokenService(secret_key="super_secret_key")
auth = AuthService(repo, hasher, token_service)

user = auth.register("abhi", "abhi@example.com", "mypassword")
user.mark_verified()

token = auth.login("abhi@example.com", "mypassword")
print("Generated Token:", token)
print("Decoded:", token_service.verify_access_token(token))
    