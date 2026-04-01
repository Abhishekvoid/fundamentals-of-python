

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



import json


def group_robots_by_status(robots):
  groups = {}
  for robot in robots:
      status = robot["status"]
      if status not in groups:
          groups[status] = []
      groups[status].append(robot)
  return groups

robots = [
    {"id": 1, "status": "active", "name": "Robot-A"},
    {"id": 2, "status": "charging", "name": "Robot-B"},
    {"id": 3, "status": "active", "name": "Robot-C"},
    {"id": 4, "status": "error", "name": "Robot-D"},
]

result = group_robots_by_status(robots)
print(json.dumps(result, indent=2))