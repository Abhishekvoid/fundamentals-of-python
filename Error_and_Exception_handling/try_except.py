
# Exceptions

"""
# Exceptions:
    - some time even if statement or expressions is syntactically correct, it may cause an error when an attempt is made to execute it. Error during execution are called Exceptions.

        - ZeroDivisionError
        - TypeError
        - NameError

        are some built in exception handlers of python
"""

# handling Exception

# example 1:

User = {"name": "ABhi", "age": 23}

# User["Role"] # as role is not declare it will show a KeyError

print("User is present ") # and as the line: 21 gives a KeyError this will not execute and the whole program will crash or will no execute bcoz of one error, to handle this we use try and except

# example 2: Try and Except

client = {"name" : "jeet", "age": 44}

try:
    client["role"]
except:
    print("the data you want to access does not present")

print("client is browsing")

# output 
"""
>>> User is present 
>>> the data you want to access does not present
>>> client is browsing

- try and except will make sure your system don't crash bocz of a single error. 
"""


# example 3:

class email_validation:

    def validate(self, email):

        try:
            if "@" not in email:
                raise ValueError("invalid email")
            print("email is not valid")
            return True
        except ValueError as e:
            print("error: ", e)
            return False
        

class register(email_validation):
    
     def save(self, data):
         
        try:
            if data:
                print("saving the user")
        except ValueError as e:
            raise ValueError("user is invalid", e)
        else: 
            ("i m else")


email = "abhigmail.com"
email_validate = email_validation()
result = email_validate.validate(email)
print(result)

register_save = register()
register_save.save(result)
# example 4:
        