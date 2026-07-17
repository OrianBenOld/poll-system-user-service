from datetime import date
from typing import Optional
from pydantic import BaseModel

# -- class user --
class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    age: int
    address: str
    joining_date: date
    is_registered: bool = False


class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None
    address: Optional[str] = None
    joining_date: Optional[date] = None
    is_registered: Optional[bool] = None

class User(UserBase):
    id: int
