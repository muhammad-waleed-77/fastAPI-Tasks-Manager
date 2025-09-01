from pydantic import BaseModel
import uuid
from enum import Enum
from datetime import datetime


class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class Status(str, Enum):
    pending = "pending"
    in_progress = "in-progress"
    completed = "completed"


class TaskBase(BaseModel):
    title: str
    description: str | None = None
    deadline: datetime
    priority: Priority


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    deadline: datetime | None = None
    priority: Priority | None = None
    status: Status | None = None


class TaskPublic(TaskBase):
    taskid: uuid.UUID
    status: Status
    created_at: datetime
    updated_at: datetime | None
    ownerid: uuid.UUID

    class Config:
        from_attributes = True
