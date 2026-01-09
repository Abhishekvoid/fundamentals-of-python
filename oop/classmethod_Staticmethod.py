
class User:

    def __init__(self, user_id, username, age) :

        self.user_id = user_id
        self.username = username
        self.age = age

    @classmethod
    def dict_data(cls, user_data): # cls will point to the main class and its data, and this will return user data in dict form 
        return (cls(

            user_data["user_id"],
            user_data["username"],
            user_data["age"],
        ))
    
class UtilsUser:
    
    @staticmethod
    def is_valid_id(user_id):
        return user_id in ["2", "4", "4"]
    

print(UtilsUser.is_valid_id("2"))
user_dict = User.dict_data({"user_id": "2", "username": "Abhi", "age": "34"})
print(user_dict.__dict__)