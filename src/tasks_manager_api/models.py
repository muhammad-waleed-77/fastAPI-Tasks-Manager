from pydantic import BaseModel, EmailStr
from sqlmodel import SQLModel, Field
from typing import Literal
import uuid 
from enum import Enum
from datetime import datetime, timezone

""" User Schema  """

# this model has common fields which others also can inherit
class UserBase(SQLModel):
    username: str 
    email: EmailStr = Field(unique=True, index=True)
   


# this modle is defining schema for creating user
class UserRegister(SQLModel):
    username: str 
    email: EmailStr = Field(unique=True, index=True)
    password: str = Field(min_length=8)


class Role(str, Enum):
    user = "user"
    admin = "admin"

# schema of User table in DB
class UserTable(UserBase, table=True):
    user_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    role: Role = Field(default=Role.user)
    hashed_password: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


# schema to define what will be displayed to user when he send a get request
class UserPublic(UserBase):
    user_id: uuid.UUID
    role: Role
    

# admin can see all users
class UsersPublic(SQLModel):
    users: list[UserPublic]
    count: int


# user can update his credentials 
class UserUpdateMe(UserBase):
    password: str = Field(min_length=8)


class AdminUpdateRole(SQLModel):
    role: Role = Field(default=Role.user)


"""  Tasks Schema   """
class TaskBase(SQLModel):
    


    


