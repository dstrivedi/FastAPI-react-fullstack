from pydantic import BaseModel
from typing import Optional

# Imports data types and column definitions from SQLAlchemy.
from sqlalchemy import Column, Integer, String

# This Base is created using declarative_base() and is the parent class for all your models.
# Every model class must inherit from this Base to register with SQLAlchemy’s ORM.
from database import Base

class TODO(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
    
# Inherits from Base, which makes it a SQLAlchemy model.
# This class will be mapped to a table in your MySQL database.
class Users(Base):
    # Specifies the name of the table in your MySQL database.
    # This tells SQLAlchemy: "map this class to the users table".
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    email = Column(String(255))
    age = Column(Integer)