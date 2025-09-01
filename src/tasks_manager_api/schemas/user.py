from pydantic import BaseModel, EmailStr
import uuid
from enum import Enum


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
