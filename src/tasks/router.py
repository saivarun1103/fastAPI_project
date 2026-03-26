from fastapi import APIRouter, Depends, status
from src.tasks import controller
from src.tasks.dtos import TaskSchema, TaskResponseSchema
from src.utils.db import get_db
from typing import List
from sqlalchemy.orm import Session
from src.utils.helpers import is_authenticated
from src.user.models import UserModel

task_routes = APIRouter(prefix="/tasks")

@task_routes.post("/create", response_model = TaskResponseSchema, status_code = status.HTTP_201_CREATED)
def create_task(body:TaskSchema,db:Session = Depends(get_db), user:UserModel = Depends(is_authenticated)):
    return controller.create_task(body, db, user)

@task_routes.get("/get", response_model = List[TaskResponseSchema], status_code = status.HTTP_200_OK)
def get_tasks(db:Session = Depends(get_db), user:UserModel = Depends(is_authenticated)):
    return controller.get_tasks(db, user)

@task_routes.get("/get_one_task/{id}", response_model = TaskResponseSchema, status_code = status.HTTP_200_OK)
def get_by_id(id: int, db:Session = Depends(get_db), user:UserModel = Depends(is_authenticated)):
    return controller.get_by_id(id, db, user)

@task_routes.put("/update_task/{id}",response_model = TaskResponseSchema, status_code = status.HTTP_201_CREATED)
def update_task(body : TaskSchema, id : int, db:Session = Depends(get_db), user:UserModel = Depends(is_authenticated)):
    return controller.update_task(body, id, db, user)

@task_routes.delete("/delete_task/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_task(id : int, db:Session = Depends(get_db), user:UserModel = Depends(is_authenticated)):
    return controller.delete_task(id, db, user)