# ✅ FastAPI: Creates your API app.
# ✅ Depends: Used for dependency injection (e.g., passing the DB session).
# ✅ HTTPException: Allows you to return HTTP error codes (like 404).
from fastapi import FastAPI, Depends, HTTPException

# ✅ engine: Your connection to the database (used to create tables).
# ✅ SessionLocal: A factory to create new DB sessions for each request.
from database import engine, SessionLocal

from schema import UserCreate, UserOut
import crud

# ✅ Base: Used to generate your tables.
# ✅ Users: The SQLAlchemy model of your users table.
from models import Base, Users

# ✅ This type hint tells FastAPI what kind of object your db dependency should return.
from sqlalchemy.orm import Session

from fastapi.middleware.cors import CORSMiddleware

# ✅ Starts a new FastAPI app instance.
app = FastAPI()

# ✅ Tells SQLAlchemy to create all tables in the database defined by your models.
# If the tables already exist, it does nothing (non-destructive).
Base.metadata.create_all(bind=engine)

# ✅ This function will be injected into your routes using Depends().
# It ensures that:
    # A DB session is created for the request.
    # It is automatically closed afterward.
    # yield db is a generator — this is FastAPI’s way of handling dependencies with cleanup.
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
        
origins = [
    "http://localhost:3000"
]

# This allows requests from your React frontend (running on localhost:3000) to the FastAPI backend (running on localhost:8000).
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)
        
@app.post("/users/", response_model=UserOut)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.get("/users/", response_model=list[UserOut])
async def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@app.get("/users/{user_id}", response_model=UserOut)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.delete("/users/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message" : "User with id {user_id} deleted"}