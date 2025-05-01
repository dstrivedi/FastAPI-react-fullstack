# This is the base class for creating data validation schemas in FastAPI.
from pydantic import BaseModel

#  Allows you to declare fields that are not required (e.g., description: Optional[str] = None).
from typing import Optional

# A base schema class that holds fields common to both request and response.
# Shared fields between input and output
class UserBase(BaseModel):
    name: str
    email: Optional[str] = None
    age: int
    
# This schema is used for incoming POST requests.
# Inherits from UserBase — so it already has name, email, and age.
# Does not include id, because the client doesn’t send it (the DB generates it).
# For user creation (POST request)
class UserCreate(UserBase):
    pass # Same as UserBase, no 'id' yet because it will be auto-generated

# Used for output (response model) in a GET request.
# Adds id, because the database assigns it.
class UserOut(UserBase):
    id: int
    
    #  Tells Pydantic: "It's OK to receive a SQLAlchemy object and still parse it like a dict".
    # Without this, FastAPI wouldn’t know how to serialize SQLAlchemy objects.
    class Config:
        orm_mode = True
        
# Class	          Purpose	    Includes id?	Used for
# UserBase	    Common fields	   ❌	      Internal use
# UserCreate    Input schema	   ❌	         POST
# UserOut	    Output schema	   ✅	         GET

# Yes — it's important and best practice to create schemas.py with Pydantic models in a FastAPI app.
# It improves validation, security, and keeps your codebase clean