
"""
User Registration Pipeline

Problem:
    - Write a function to collect user data (username, email, password)
    - Write a validator function
    - Write a save function   
    - Use a controller function to orchestrate

Constraints:
    - Validation must be a pure function
    - Save must be impure
    - No globalsUser Registration Pipeline

"""


def get_user():
    return {
        "username" : input("enter your username here: ").striabp(),
        "email": input("enter your valid email here: ").strip(),
        "password": input("enter your password here: ")
    }
   


def validator(data):

    if not isinstance(data, dict):
        return False, "invalid data format"
    
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username:
        return "username field is required"
    
    if "@" not in email:
        return "invalid email..."
    
    if len(password) < 8:
        return "password is not strong"
    
    return True, "validation passed"


def saving_to_db(data):

    print(f"saving user to database...")
    print(f"username: {data["username"]}")
    print(f"Email: {data["email"]}")


def control():

    data = get_user()
    is_valid, message = validator(data)

    if not is_valid:
        print(f"Error: {is_valid}, {message}")
        return
    
    saving_to_db(data)
    print(f"used user successfully")

control()