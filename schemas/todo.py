from pydantic import BaseModel, Field

class Todo(BaseModel):

    id: int | None = Field(None, description='Primary key')
    title:str
    description:str

    class Config:
        from_atributes = True

class TodoListOut(BaseModel):

    list:list[Todo]
    total_count:int