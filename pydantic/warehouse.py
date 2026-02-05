from pydantic import BaseModel, field_validator, model_validator, Field
from typing import Union, Literal

class MoveCommand(BaseModel):
   
    command_type: Literal['move'] 
    x: float
    y: float

    @field_validator('x', 'y')
    @classmethod
    def value_validator(cls, v: float) -> float:
        if v < 0: 
            raise ValueError('Value cannot be negative')
        return v
         
class PickCommand(BaseModel):
    command_type: Literal['pick']
    package_id: str
    package_weight: float
    pressure: float

    @field_validator('package_id') 
    @classmethod
    def pkg_id_validator(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError('package_id cannot be empty')
        return v.upper()

    @model_validator(mode='after')
    def check_safety_logic(self) -> 'PickCommand':
        if self.pressure > 80 and self.package_weight < 5.0:
            raise ValueError(
                f"Safety Risk: High pressure ({self.pressure}) "
                f"cannot be used on light package ({self.package_weight}kg)"
            )
        return self

class RobotInstruction(BaseModel):
   
    action: Union[MoveCommand, PickCommand] = Field(discriminator='command_type')