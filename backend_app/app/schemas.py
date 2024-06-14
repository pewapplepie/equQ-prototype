from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class ProgramCreate(BaseModel):
    title: str
    description: str
    application_deadline: Optional[str] = None
    curriculum: Optional[str] = None

class Program(BaseModel):
    id: int
    title: str
    description: str
    application_deadline: Optional[str] = None
    curriculum: Optional[str] = None

    class Config:
        from_attributes = True
