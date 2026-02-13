
class User:

    def __init__(self, username, email):
        self.username = username
        self.email = email
    
    def display_user(self):

        return (f"username is: {self.username} and email id is: {self.email}")


user_data = User("abhis", "irgbfworeg")
print(user_data.display_user())