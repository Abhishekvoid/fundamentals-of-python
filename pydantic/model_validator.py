from pydantic import BaseModel, Field, field_validator, model_validator
from typing import List
from enum import Enum
from datetime import datetime


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


# prblem 3.

class MenuUpdate(BaseModel):
    
    item_id: str
    price = float =  Field(gt=0)
    discounted_price = float = Field(gt=0)

    @model_validator(mode='after')
    def check_discounted_price(self) -> 'MenuUpdate':

        if self.discounted_price >= self.price:

            raise ValueError("discounted must be lower than the original price")
        return self
    

# problem 4.

class LoyaltySignup(BaseModel):

    referral_code = str

    @field_validator('referral_code', mode='before')
    def format_referral(cls, v:str) -> str:

        if isinstance(v, str):
            return v.strip().upper()
        return v
    

# problem 5.

class RobotArmCommand(BaseModel):

    joint_id: int
    angle_degree: float = Field(ge=-180, le=180)

    @field_validator('angle_degree')
    def check_safety_stop(cls, v:float) -> float:

        if 170 < abs(v) <= 180:
            print(f"Warning: Approaching physical limit at {v}°")
        return v        
    
class ExtractedMetadata(BaseModel):
    source_url: str
    publish_date: datetime

    @field_validator('publish_date')
    @classmethod
    def ensure_not_future(cls, v: datetime) -> datetime:
        # LLMs sometimes hallucinate dates like 2099-01-01
        if v > datetime.now():
            raise ValueError("Extracted date cannot be in the future.")
        return v