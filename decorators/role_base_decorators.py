
from functools import wraps
def role_auth(role):

    @wraps(role)
    def wrapper(user_role, *args, **kwargs):
        if user_role != "admin":
            print("Access denied: admins only")
        else:
            return role(user_role, *args, **kwargs)
            
    return wrapper
    


@role_auth
def acessing(role):
    print("providing the access")

acessing("admin")