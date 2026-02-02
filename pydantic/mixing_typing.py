from  pydantic import BaseModel
from typing import Dict, List, Optional 
from datetime import datetime

class User(BaseModel):

    id: int
    name: str
    email: Optional[str] = None  # can be optional and can be none
    signup_ts: datetime
    tag: List[str] = [] # will be a list of string
    metadata: Dict[str, int] = {} # will be a dictionary with string and integer pair


dirty_data = {
    "id": "123",                    # str → int
    "name": "Abhi", 
    "signup_ts": "2026-02-02 10:00",  # str → datetime
    "tags": ["gold", 2, "active"],    # 2 → "2" (coerced)
    "points": 150                    # Extra field ignored
}

user = User(**dirty_data)
print(user) # output: id=123 name='Abhi' email=None signup_ts=datetime.datetime(2026, 2, 2, 10, 0) tag=[] metadata={}
print(type(user.tag)) # list