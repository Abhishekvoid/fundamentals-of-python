

"""
 # dict coomperhensions
   - create dictionary in one line 

 # syntax 
   - {key:value for item in iterable}
 
 # with conditions
   - {key:value for item in iterable if conditon}
"""


# basic example

numbers = {1,2,3}
squares = {x: x*x for x  in numbers}
print(squares)

# real-world example

users = [
    {"name": "joy", "age": 40, "status": "in-active", "email": "abhi@gmail.com"},
    {"name": "megan", "age": 31, "status": "active", "email": "ayuuu@gmail.com"},
    {"name": "fish", "age": 21, "status": "active", "email": "goldfish@gmail.com"},
    {"name": "fox", "age": 11, "status": "active", "email": "articfox@gmail.com"},
]

email_to_name = {user["email"]: user["name"] for user in users}
print(email_to_name)