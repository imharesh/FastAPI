from pydantic import BaseModel, EmailStr
from typing import List, Optional
from uuid import UUID

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: str  # Change to str for proper serialization
    username: str
    email: EmailStr

    class Config:
        orm_mode = True
        
class ProductCreate(BaseModel):
    name: str
    description: Optional[str]
    price: float

class ProductOut(BaseModel):
    id: UUID
    name: str
    description: Optional[str]
    price: float

    class Config:
        orm_mode = True


class BusinessCreate(BaseModel):
    name: str
    location: str
    email: EmailStr
    owner_name: str
    products: Optional[List[ProductCreate]] = []

class BusinessOut(BaseModel):
    id: UUID
    name: str
    location: str
    email: EmailStr
    owner_name: str
    products: List[ProductOut] = []

    class Config:
        orm_mode = True