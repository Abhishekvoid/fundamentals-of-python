

def get_user_input():
 
    username = input(f"enter your username here: ").strip()
    email = input(f"enter your valid email here: ").strip()
    password = input(f"enter your password here: ")
    
    return username, email, password

def validate_input():

    return (f"validating User data....")

def save_to_db():

    print(f"saving the user in db...")

def register_user():

    validator =  validate_input()
    saving = save_to_db()

    

    username, email, password = get_user_input()
    

    print(f"Username: {username}")
    print(f"Email: {email}")
    print(f"Hashed Password: {password}")
    print(validator)
    print(saving)
    
    
    



register_user()