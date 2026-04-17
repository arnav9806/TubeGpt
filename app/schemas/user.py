from pydantic import BaseModel, EmailStr
from datetime import datetime


# Request schema (register)
class UserCreate(BaseModel):
    email: EmailStr
    password: str


# Response schema
class UserResponse(BaseModel):
    id: int
    email: str
    role: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True