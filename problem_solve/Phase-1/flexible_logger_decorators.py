"""
2️⃣ Flexible Logger
Problem:
    - Write a decorator that logs:
        - function name
        - arguments passed

    - It must work for ANY function
    -   Preserve function metadata

Hint: *args, **kwargs, @wraps
"""

from functools import wraps

def logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"calling... {func.__name__}")
        result = func(*args, **kwargs)
        print(f"finished... {func.__name__}")
        return result
    return wrapper

