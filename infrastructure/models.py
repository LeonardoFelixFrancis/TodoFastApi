from .database import Base
from sqlalchemy import Column, String, Integer

class Todo(Base):

    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)

