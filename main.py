from fastapi import FastAPI
from api.routes import todo

from infrastructure.database import SessionLocal, engine
from infrastructure import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(todo.router)

@app.get("/")
def root():
    return "Hello World"