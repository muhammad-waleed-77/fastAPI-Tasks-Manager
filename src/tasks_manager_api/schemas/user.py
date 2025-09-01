from pydantic import BaseModel, EmailStr
import uuid
from enum import Enum
from sqlmodel import SQLModel, Field

class Role(str, Enum):
    user = "user"
    admin = "admin"


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserRegister(UserBase):
    password: str


class UserPublic(UserBase):
    user_id: uuid.UUID
    role: Role

    class Config:
        from_attributes = True


class UsersPublic(BaseModel):
    users: list[UserPublic]
    count: int

    class Config:
        from_attributes = True


class UserUpdateMe(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    password: str | None = None


class AdminUpdateRole(BaseModel):
    role: Role = Role.user


class AdminRegister(SQLModel):
    username: str
    email: EmailStr = Field(unique=True)
    hashed_password: str = Field(min_length=8)
    role: Role = Role.admin  # always admin