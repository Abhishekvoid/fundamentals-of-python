from pydantic import BaseModel, Field, ConfigDict, field_validator
from typing import Optional, Literal
from datetime import datetime, timezone
from uuid import UUID, uuid4
from enum import Enum
import re

class ContainerStatus(str, Enum):
    ARRIVED = "arrived"
    IN_YARD = "in_yard"
    LOADED = "loaded"
    DEPARTED = "departed"
    BLOCKED = "blocked"

class YardZoneType(str, Enum):
    IMPORT = "import"
    EXPORT = "export"
    HAZARDOUS = "hazardous"
    REEFER = "reefer"
    EMPTY = "empty"

class Container(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        str_to_lower=True,
        extra='forbid'
    )
    
    id: Optional[UUID] = Field(default_factory=uuid4)
    container_number: str = Field(..., min_length=10, max_length=11, pattern=r'^[A-Z]{3}[U]?[0-9]{7}[A-Z0-9]$')
    shipping_line: str = Field(..., min_length=2, max_length=30)
    status: ContainerStatus = Field(default=ContainerStatus.IN_YARD)
    yard_zone: str = Field(..., min_length=1, max_length=10)
    row: str = Field(..., pattern=r'^[A-Z]{1,3}\d{1,3}$')  # A1, B23, etc.
    stack_level: int = Field(ge=1, le=8)
    last_updated: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    
    @field_validator('container_number')
    @classmethod
    def validate_container_number(cls, v):
        if not re.match(r'^[A-Z]{3}[U]?[0-9]{7}[A-Z0-9]$', v):
            raise ValueError('Invalid container number format (BIC standard)')
        check_digit = calculate_check_digit(v[:-1])
        if v[-1].upper() != check_digit:
            raise ValueError(f'Invalid check digit. Expected {check_digit}')
        return v.upper()

class YardZone(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        str_to_lower=True,
        extra='forbid'
    )
    
    zone_code: str = Field(..., min_length=1, max_length=10)
    zone_type: YardZoneType
    capacity: int = Field(gt=0)
    current_load: int = Field(ge=0)
    total_slots: int = Field(gt=0)
    
    @model_validator(mode='after')
    def validate_load(self):
        if self.current_load > self.capacity:
            raise ValueError('Current load exceeds capacity')
        if self.current_load > self.total_slots:
            raise ValueError('Current load exceeds total slots')
        return self

def calculate_check_digit(container_prefix: str) -> str:
    """BIC container check digit calculation"""
    weights = [21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    total = sum(int(c) * w for c, w in zip(container_prefix.upper(), weights) 
                if c.isdigit() or c.isalpha())
    return str(total % 10)
