from fastapi import FastAPI, status, HTTPException
from scalar_fastapi import get_scalar_api_reference
from typing import Any

from task_manager_app.schemas import TaskCreate



app = FastAPI()

db = {
    1: {
        "id": 1,
        "title": "finish designing the level-1 game",
        "description": "not much",
        "status": "pending",
        "due_date": "05-09-2025"
    },
    2: {
        "id": 2,
        "title": "finish designing the level-2 game",
        "description": "not much",
        "status": "pending",
        "due_date": "10-09-2025"
    }
}

@app.get("/tasks/latest")
def get_tasks() -> dict[str, Any]:
    max_num = len(db)
    latest_task = db[max_num]
    return latest_task

@app.get("/tasks/{id}")
def get_task_by_id(id: int) -> dict[str, Any]:
    task = db[id]
    return task

@app.post("/tasks")
def create_task(body: TaskCreate) -> dict[str, str]:
    new_task_id = len(db) + 1
    db[new_task_id] = {
                        "id": new_task_id,
                        "title": body.title,
                        "description": body.description,
                        "status": body.status,
                        "due_date": body.due_date
                    }
    
    return {
        "detail": f"new task created with id {new_task_id}"
    }



@app.get("/scalar")
def get_scalar_docs():
    return get_scalar_api_reference(openapi_url=app.openapi_url,title="Task Manager API")