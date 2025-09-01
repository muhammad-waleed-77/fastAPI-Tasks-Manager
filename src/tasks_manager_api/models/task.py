from sqlmodel import SQLModel, Field, Relationship
import uuid
from enum import Enum
from datetime import datetime, timezone
from typing import Optional

class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class Status(str, Enum):
    pending = "pending"
    in_progress = "in-progress"
    completed = "completed"


class TaskTable(SQLModel, table=True):
    taskid: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str
    description: str | None = Field(default=None, max_length=100)
    deadline: datetime
    priority: Priority
    status: Status = Field(default=Status.pending)
    ownerid: uuid.UUID = Field(foreign_key="usertable.user_id", nullable=False)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column_kwargs={"onupdate": datetime.now(timezone.utc)} 
    )

    owner: Optional["UserTable"] = Relationship(back_populates="tasks") # it is only relationship not DB table

