

def create_user():

    return {

        "username": input("enter your username: "),
        "email" : input("enter your email: "),
        "password": input("enter your password: ")
    }


def validator(data):

    
    if not isinstance(data, dict):
        return False, "invalid input format"

    username =  data.get("username")
    email = data.get("email")
    password = data.get("password")
   
    if not username:
        return False, "Username is required"
        
    if "@" not in email:
        return False, "Invalid email"

        
    if len(password) < 8:
        return False, "Password is too weak"
    
    
    return True, "validation passed"


def saving_to_db(data):

    print("Saving user to the database...")
    print(f"Username: {data['username']}")
    print(f"Email: {data['email']}")


def printing():

    data = create_user()
    is_valid, message = validator(data)


    if not is_valid:
        print(f"Error: {message}")
        return
    
    saving_to_db(data)
    print("user saved succesfully")

printing()
