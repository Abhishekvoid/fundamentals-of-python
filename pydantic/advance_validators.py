
# 1. multi-field Dependencies
# This is when one field’s validity depends on another

"""
 - A delivery app cannot allow a "Scheduled Delivery Time" to be earlier than the "Order Creation Time
"""

from pydantic import BaseModel, model_validator, field_validator, AfterValidator, Field 

from datetime import datetime
from typing import Annotated, Union, Literal

class Order(BaseModel):

    created_at: datetime
    schedule_for: datetime

    @model_validator(mode='after')
    def check_time(self) -> 'Order':
        if self.schedule_for > self.created_at:
            raise ValueError("You can't schedule a delivery in the past!")
        return self
    
# 2. Pre-Parsing Logic 
"""

If your LLM returns a string "True" instead of a boolean True, or a string "90%" instead of a float 0.9, you use mode='before' to fix it.
"""

class QuizScore(BaseModel):

    score: float

    @field_validator(score, mode='before')
    @classmethod
    def clean_data(cls, v):
        if isinstance(v, str) and "%" in v:
            return float(v.replace("%", "")) / 100
        return v 
    
      
# 3. Resuable Validators

# Ensuring a motor ID is always within the valid CAN-bus range (1-127).


def validate_motor_id(v: int) -> int:

    if v < 1 or v > 127:
        raise ValueError("Motor ID must be between 1 and 127")
    return v


MotorID = Annotated[int, AfterValidator(validate_motor_id)]

class RobotConfig(BaseModel):
    arm_id = MotorID
    leg_id  = MotorID



# 4. Discriminated Unions

# If the agent calls search, it needs a query. If it calls calculator, it needs expression

class SearchTool(BaseModel):

    type: Literal['search']
    query: str

class CalculatorTool(BaseModel):

    type: Literal['calc']
    expression: str

class AgentAction(BaseModel):

    action: Union[SearchTool, CalculatorTool] = Field(discriminator='type')     