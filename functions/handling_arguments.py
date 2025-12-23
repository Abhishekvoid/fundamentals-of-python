
# handling argument



# 2. *args -- Variable Positional Arguments
# "accepts any number of positional arguments"

def add(*args):
    print(args)

add(1,2,3)
add(5, 10, 20, 30)

"""

Why '*'?

the '*" tells python:
    "Collect all extra positional agruments into a tuple"

"""

def log(*messages):
    for msg in messages:
        print(msg) 


"""
3. **Kwargs -- variable keyword Arguments

meaning:
    "Accept any number of named arguments"
"""

def show_user(**kwargs):
    print(kwargs)

show_user(name="Abishkek", age=23, role="Dev")


# some real world examples of *args and **kwargs

# 1. logging system 

# problem: we dont know how many msg or details we'll log. solution using *args

def log(*messages):
    for msg in messages:
        print(msg)

log("user created", "Id = 72", "status=active")



# 2. User Registration (API/backend)

# Problem: User data may change (today name/email, tomorrow phone/address).

def create_user(id, is_active, **user_data):
    

    if id == "1" and is_active == True:
        print(f"{id} is present and here is data: {user_data}")
    else:
        print(f"the id is not valid")

 
create_user (
    id = "1",
    username = "Ayushi",
    email = "ayuu@gmail.com",
    role = "desginer",
    is_active = True,
)

# why ** ?

# "collect all keyword arguments inta a dictionary"


"""
4. using *args and **kwargs

"""

def recipt(*cart, **user_list):

    print(f"cart data: {cart}")  # using * any number of poisiitnal arguments
    print(f"user_list data: {user_list}") # using ** any number of named arguments


recipt(1, "bread", "toothpaste", name = "abhishek", total = 100)


# changing values in the function 

def changing_name(name):
    name  = "riya"
    return (f"we changed the name in the function checking the mutability: {name}")


name = "abhishek"
print(f"data before changing the name in the function: {name}")
print( changing_name(name))