"""
Problem:

Given a list of users (dicts)
Return:
    - list of all emailsx
    - set of unique emails
    - dict mapping email → username

Constraint:
Use comprehensions only (no loops)

"""


users = [
    {"name": "joy", "age": 40, "status": "in-active", "email": "abhi@gmail.com"},
    {"name": "megan", "age": 31, "status": "active", "email": "ayuuu@gmail.com"},
    {"name": "fish", "age": 21, "status": "active", "email": "goldfish@gmail.com"},
    {"name": "fox", "age": 11, "status": "active", "email": "articfox@gmail.com"},
]

email_extract  = {user["email"]: user["name"] for user in users}
print(f"{email_extract}")