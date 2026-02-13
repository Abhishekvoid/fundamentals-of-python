


# a normal loop function
squares = []
for x in range(5):
    squares.append(x*x)
print(f"normal loop function: {squares}")


# List comprehensions

comp_squares = [x*x for x in range(5)]
print(f"after the list comperhensions: {comp_squares}")

"""
    Same result
    Less code
    More readable
"""

# basic structure is [expressions for item in iterable]

evens = []
for x in range(5):
    if x % 2 == 0:
        evens.append(x)
print(f"normal loop function: {evens}")

comp_evens = [x for x in range(5) if x %2 == 0]
# [expressions for item in iterable if condition]
print(f"after the list comperhensions: {comp_evens}")
    

users = [
    {"name": "joy", "age": 40, "status": "in-active", "email": "abhi@gmail.com"},
    {"name": "megan", "age": 31, "status": "active", "email": "ayuuu@gmail.com"},
    {"name": "fish", "age": 21, "status": "active", "email": "goldfish@gmail.com"},
    {"name": "fox", "age": 11, "status": "active", "email": "articfox@gmail.com"},
]

emails = []
for user in users:
    if user["status"] == "active":
        emails.append(user["email"])

print (emails)

comp_emails = [user["email"] for user in users if user["status"] == "active"]
print(comp_emails) 

comp_age = [user["name"] for user in users if user["age"] >= 18]
print(comp_age)

"""
    as we need the email of the users which are active... we pass our need in the expression.
    example: user["email"] and user [name"]
"""