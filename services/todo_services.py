from typing import Annotated, Any
from repositories.todo_repository import TodoRepository
from schemas.todo import Todo
from fastapi import Depends, HTTPException

class TodoServices:

    def __init__(self, infrastrucutre: Annotated[TodoRepository, Depends(TodoRepository)]):
        self.infrastructure = infrastrucutre

    def create_todo(self, todo:Todo) -> None:
        return self.infrastructure.create(todo)

    def update_todo(self, todo:Todo) -> Todo:

        existing_todo = self.read_todo(todo.id)

        if existing_todo is None:
            raise HTTPException(status_code=404, detail="Item not found")

        updated_instance = self.infrastructure.update(todo)

        return updated_instance

    def read_todo(self, todo_id:int) -> Todo | None:
        todo = self.infrastructure.read(todo_id)

        return todo
    
    def delete_todo(self, todo_id:int) -> Todo: 

        todo = self.read_todo(todo_id)

        if todo is None:
            raise HTTPException(status_code=404, detail="Item not found")
        
        self.infrastructure.delete(todo)

        return todo

    def list_todo(self, skip:int | None, take:int | None) -> list[Todo]:
        return self.infrastructure.list(skip, take)
