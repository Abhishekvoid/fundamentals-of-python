

# base Model

from pydantic import BaseModel, Field, field_validator, model_validator, ConfigDict

class CreateUser(BaseModel):
    
    name: str
    age: int
    email: str
    
    
user  = CreateUser(name="Ayushi", email="ayu@gmail.com", age=21)
# if data type didn't match it will throw validation error

print (user)

# field

class OrderModel(BaseModel):
    
    itemName: str = Field(
        ...,
        min_length = 3,
        max_length = 256
    )
    price: int = Field(
        ...,
        gt=100,
        lt=500
    )
    
Order = OrderModel(itemName="kaju masala", price = 499)
# if data type and fileds constraints didn't match it will throw validation error

print(Order)


# field Validator


class CreateEmail(BaseModel):
    
    email: str
    
    @field_validator("email")
    @classmethod
    def email_validator(cls, value:str) -> str:
        
        if not value.endswith("@company.com"):
            raise ValueError(
                "only company emails allowed"
            )
        
        return value
    
# model validator

class confirm_password(BaseModel):
    
    password: str
    confirm_password: str
    
    @model_validator(mode="after")
    def password_match(self):
        
        if self.password != self.confirm_password:
            raise ValueError("passwords do not match")
        
        return self
    
 
# model_config

class UserId(BaseModel):
    
    model_config = ConfigDict(
        strict =True
    )
    
    age: int