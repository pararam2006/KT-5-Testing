from pydantic import BaseModel, EmailStr
from typing import Optional


class User(BaseModel):
    id: int
    username: str
    firstName: str
    lastName: str
    email: EmailStr
    password: str
    phone: str
    userStatus: int


class Order(BaseModel):
    id: int
    petId: int
    quantity: int
    shipDate: str
    status: str
    complete: bool
