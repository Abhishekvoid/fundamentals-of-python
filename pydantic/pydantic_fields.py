from pydantic import BaseModel, Field
from typing import List

# class Customer(BaseModel):

#     phone: str = Field(..., pattern="^\+91\d{10}$")             # required + regex
#     name: str = Field(..., min_length=2, max_length=50)         # length Limits
#     age: int = Field(ge=18, le=100)                             # range from 18 to 100
#     points: float =Field(gt=0, le=10000)                        # positive float
#     is_vip: bool =  True                                        # default value = true
#     tags: List[str] = Field(default_factory=list)               # empty list


# # These FAIL with clear errors:
# Customer(phone="123", name="A")        # name too short
# Customer(age=15)                       # age < 18  
# Customer(points=-10)                   # points < 0



class OrderItem(BaseModel):

    name: str =  Field(..., min_length=1)                        # required
    price: float = Field(gt=0)                                   # positive price
    qty: int = Field(ge=1, le=10)                                # min = 1, max = 10

class Order(BaseModel):

    customer: str = Field(..., pattern=r"^\+91\d{10}$")
    restaurant_id: int = Field(gt=0)
    items: List[OrderItem] = Field(min_length=1)  # At least 1 item

    @property    
    def total(self) -> float:
        return sum(item.price * item.qty for item in self.items )
    
order = Order(
    customer="+919876543210",
    restaurant_id=1,
    items=[{"name": "Biryani", "price": 250, "qty": 2}]
)

print(order.total)