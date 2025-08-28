from pydantic import BaseModel, Field
from enum import Enum

class TaskStatus(Enum):
    pending: str = "pending"
    done:str = "done"

class TaskCreate(BaseModel):
    title: str = Field(description="Title of the Task")
    description: str = Field(description="Decsription of the Task")
    status: TaskStatus = Field(description="Status of the Task")
    due_date: str = Field(description="Due date for the Task")