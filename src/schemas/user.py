from enum import Enum
from typing import Optional
from pydantic import BaseModel, EmailStr


class NewUser(BaseModel):
    fullname: str
    email: EmailStr


class User(NewUser):
    # Чтоб можно было использовать Customer когда его нет в БД id будет необязательным
    id: Optional[int] = None


class Customer(User):
    pass


class Role(Enum):
    Administrator = "Администратор"
    Pharmacist    = "Фармацевт"
    Cleaner       = "Уборщик"


class Employee(User):
    role: Role


class UserLoginData(BaseModel):
    # Здесь просто нет id, так как он не нужен. Email сам по себе PK 
    email: EmailStr
    code: int
