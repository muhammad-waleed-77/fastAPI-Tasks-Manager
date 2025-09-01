from sqlmodel import SQLModel, Field, Relationship
import uuid
from enum import Enum
from datetime import datetime, timezone
from typing import List
from pydantic import EmailStr


class Role(str, Enum):
    user = "user"
    admin = "admin"




class UserTable(SQLModel, table=True):
    user_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    username: str
    email: str = Field(unique=True, index=True)
    hashed_password: str
    role: Role = Field(default=Role.user)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    tasks: List["TaskTable"] = Relationship(back_populates="owner")  # it is only relationship not DB table


"""
initially i will be creating DB table with Metadata.createall(..) but in later stage when i have to add new column
it will not work if i run again--- so here comes ALEMBIC --- for handling migrations in DB

alembic revision --autogenerate -m "add priority column to tasks"      --- (add new column in table) generates migration file
alembic upgrade head  --- update the table

"""