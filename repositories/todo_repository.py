from pydantic import BaseModel
from schemas.todo import Todo
from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from infrastructure.database import get_db
from infrastructure import models

class TodoRepository():

    def __init__(self, db: Annotated[Session, Depends(get_db)]):
        self.db = db

    def create(self, instance:Todo) -> Todo:
        
        db_instance = models.Todo(**instance.model_dump())
        self.db.add(db_instance)
        self.db.commit()
        self.db.refresh(db_instance)

        return db_instance


    def update(self, instance:Todo) -> Todo:
        print(instance)
        self.db.query(models.Todo).filter(models.Todo.id == instance.id).update({"title":instance.title, "description":instance.description})
        self.db.commit()
        return instance

    def read(self, instance_id:int): 
        return self.db.query(models.Todo).filter(models.Todo.id == instance_id).first()
         

    def delete(self, instance:Todo):
        
        self.db.query(models.Todo).filter(models.Todo.id == instance.id).delete()
        self.db.commit()

        return instance

    def list(self, skip:int | None=0, take: int | None=10):
        count = self.db.query(models.Todo).count()
        return {"data":self.db.query(models.Todo).limit(take).offset(skip), "total_amount":count}
    