from pydantic import BaseModel, EmailStr
from sqlmodel import SQLModel, Field, Relationship
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
    email: EmailStr 
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
    tasks: list["TaskTable"] = Relationship(back_populates="owner")


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
    username: str | None = None
    email: EmailStr | None = None
    password: str = Field(default=None, min_length=8)


class AdminUpdateRole(SQLModel):
    role: Role = Field(default=Role.user)


"""  Tasks Schema   """
# common fields

class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class Status(str, Enum):
    pending = "pending"
    in_progress = "in-progress"
    completed = "completed"


class TaskBase(SQLModel):
    title: str 
    description: str = Field(default=None, max_length=100)
    deadline: datetime
    priority: Priority 
    
    

# model to create tasks
class TaskCreate(TaskBase):
    pass
    

class TaskUpdate(TaskBase):
    title: str | None = None
    description: str | None = None
    deadline: datetime | None = None
    priority: Priority | None = None
    status: Status = Field(default=Status.pending)
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class TaskTable(TaskBase, table=True):
    taskid: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    status: Status = Field(default=Status.pending)
    ownerid: uuid.UUID = Field(foreign_key="usertable.user_id", nullable=False)
    ownername: str = Field(foreign_key="usertable.username")
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default=None)
    owner: UserTable | None = Relationship(back_populates="tasks")


class TaskPublic(TaskBase):
    created_at: datetime
    updated_at: datetime
    taskid: uuid.UUID
    ownerid: uuid.UUID
    ownername: str





    




    
    


    



    


