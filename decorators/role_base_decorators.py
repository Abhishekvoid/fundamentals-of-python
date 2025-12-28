
from functools import wraps
def role_auth(role):

    def decorators(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if role != role:
                raise PermissionError("access denied")
            return func(user, *args, **kwargs)
        return wrapper
    return decorators


@role_auth("admin")
def acessing(role):
    print("user deleted")

acessing("admin")