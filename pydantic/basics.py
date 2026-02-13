from pydantic import BaseModel


class User(BaseModel):

# defining the type of the data
    id: int
    name: str
    is_active: bool


# matching the type when passing the data
user_input = {'id': 2, 'name': 'Abhi', 'is_active': True}


# unpacking the user_input dict using '**'
result  = User(**user_input)
print(result)

# note: pydantic also try to convert the according to the type for example:

user_input_2 = {'id': "45", 'name': 'riya', 'is_active': False} # here as you passing a str in id which is number pydantic try to convert it to interger matching the type you define which is every possible so now, "45" string will work as integer    "45" -> 45, "true" -> True, 123 -> 123.0