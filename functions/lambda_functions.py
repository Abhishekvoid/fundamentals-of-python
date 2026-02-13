


# lambda function are anonymous functions written in one line

# normal function
def add(a, b):
    a+b

# lambda function
add = lambda a, b: a+b

"""
1. lambda is a quick function
2. no name(unless you assign it)
3. one expression only

"""

# Real world use 

# 1. sorting

users = [
    {"name": "joy", "age": 40, "status": "in-active", "email": "abhi@gmail.com"},
    {"name": "megan", "age": 31, "status": "active", "email": "ayuuu@gmail.com"},
    {"name": "fish", "age": 21, "status": "active", "email": "goldfish@gmail.com"},
    {"name": "fox", "age": 11, "status": "active"},
]

l = users.sort(key=lambda u: u["age"])
print(l)

# 2. filtering data

active_users = list(filter(lambda u: u["status"] == "active", users))
print(f"active users: {active_users}")

# 3. mapping the data

has_emails = list(map(lambda u: u["email"], filter(lambda u: "email" in u, users) ))
print(f"this users has email: {has_emails}")


last_name = ["rajput", "joshi", "tanwar", "sharma", "tanwar"]

common_last_name = list(filter(lambda last: last == "tanwar", last_name))

print(f"common last name: {common_last_name}")



# Pure function

""" 
    1. a function always return same output for same input
    2. Doest not allow to modify anything outside itself
"""

def add(a, b):
    return a+b


# impure function 

"""
    1. uses and modifies external state
    2. or depends on outside data
"""

total = 0

def add_to_total(x):

    global total
    total += x