
# set comperhensions

"""
 1. similar to the list comperhensions but it will return set
 2. set automatically remove the duplicate values
"""

# {expersion for item in iterable}

numbers  = [1, 2,2,33,33,654634, 23, 65, 23]
set_comp_numbers = {x for x in numbers }
print(set_comp_numbers)



users = [
    {"id": "1", "name": "joy", "age": 40, "status": "in-active", "email": "abhi@gmail.com"},
    {"id": "1", "name": "megan", "age": 31, "status": "active", "email": "ayuuu@gmail.com"},
    {"id": "2", "name": "fish", "age": 21, "status": "active", "email": "goldfish@gmail.com"},
    {"id": "3", "name": "fox", "age": 11, "status": "active", "email": "articfox@gmail.com"},
]

has_duplicate = len({user["id"] for user in users}) != len(users)
print(has_duplicate)