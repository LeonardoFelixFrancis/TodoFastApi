from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from schemas.todo import Todo, TodoListOut
from services.todo_services import TodoServices

router = APIRouter(
    prefix='/todo',
    tags=['todos'],
    responses={404: {"description": "Not Found"}}
)

@router.post("/")
def create_todo(todo: Todo, todo_service: Annotated[TodoServices, Depends(TodoServices)]) -> Todo:

    created_todo = todo_service.create_todo(todo)

    return created_todo

@router.get("/list")
def list_todos(skip:int|None, take:int|None, todo_service: Annotated[TodoServices, Depends(TodoServices)]) -> TodoListOut:

    todos_list = todo_service.list_todo(skip, take)

    return {
        "list":todos_list['data'],
        "total_count":todos_list['total_amount']
    }


@router.get("/{todo_id}")
def read_todo(todo_id:int, todo_service: Annotated[TodoServices, Depends(TodoServices)]) -> Todo:

    todo = todo_service.read_todo(todo_id)

    print(todo)

    if todo is None:
        raise HTTPException(status_code=404, detail='Todo not found')

    return todo


@router.put("/")
def update_todo(todo:Todo, todo_service: Annotated[TodoServices, Depends(TodoServices)]) -> Todo:

    old_title = todo.title
    old_description = todo.description
    print(todo)
    new_todo = todo_service.update_todo(todo)

    return new_todo

@router.delete("/{todo_id}")
def delete_todo(todo_id:int, todo_service: Annotated[TodoServices, Depends(TodoServices)]) -> Todo:

    deleted_todo = todo_service.delete_todo(todo_id)

    return deleted_todo

