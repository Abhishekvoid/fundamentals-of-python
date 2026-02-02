from pydantic import BaseModel, Field, field_validator, model_validator
from typing import List
from enum import Enum


# FIELD VALIDATORS: Custom Business Logic
class Customer(BaseModel):
    phone: str = Field(pattern=r"^\+91\d{10}$")
    name: str
    
    @field_validator('phone')  # Pydantic v2 syntax
    @classmethod
    def validate_phone(cls, v):
        if not v.startswith('+91'):
            raise ValueError('Indian numbers only')
        if len(v) != 13:  # +91 = 2 chars + 10 digits
            raise ValueError('Exactly 10 digits after +91')
        return v.title()  # Normalize
    
    @field_validator('name')
    @classmethod
    def validate_name(cls, v):
        return v.strip().title()
    
# MODEL VALIDATORS: Cross-Field Logic
class Order(BaseModel):
    customer: str
    restaurant_id: int
    total_amount: float
    
    @model_validator(mode='after')
    def check_total_positive(self):
        if self.total_amount <= 0:
            raise ValueError('Total must be positive')
        return self
    

class Status(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"

class OrderItem(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(gt=0)
    qty: int = Field(ge=1, le=10)
    
    @field_validator('price')
    @classmethod
    def price_must_be_positive(cls, v):
        if v > 10000:  # Sanity check
            raise ValueError('Unrealistic price')
        return v

class Order(BaseModel):
    customer: str = Field(pattern=r"^\+91\d{10}$")
    restaurant_id: int = Field(gt=0)
    items: List[OrderItem] = Field(min_length=1)
    status: Status = Status.PENDING
    
    @model_validator(mode='after')
    def calculate_total(self):
        self.total_amount = sum(
            item.price * item.qty for item in self.items
        )
        return self
