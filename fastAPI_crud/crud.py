# ✅ Session: The database session used to interact with MySQL.
# ✅ Users: The SQLAlchemy model for the users table.
# ✅ UserCreate, UserOut: Pydantic schemas to validate input/output.
from sqlalchemy.orm import Session
from models import Users
from schema import UserCreate, UserOut

# ✅ user: UserCreate → Validated input from the request body.
# db_user = Users(...) → Create a SQLAlchemy object from the Pydantic input.
# db.add(...) → Add it to the current DB session.
# db.commit() → Write changes to the database.
# db.refresh(db_user) → Update the object with any DB-generated values (like id).
# return db_user → Returns the new user to the API route.
def create_user(db: Session, user: UserCreate):
    db_user = Users(name=user.name, email=user.email, age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# ✅ Fetches all rows from the users table.
# Returns a list of Users model instances.
def get_users(db: Session):
    return db.query(Users).all()

# ✅ filter(Users.id == user_id) → WHERE clause to find the user by ID.
# first() → Return the first match or None.
def get_user(db: Session, user_id: int):
    return db.query(Users).filter(Users.id == user_id).first()

# ✅ Get the user by ID.
# If found, delete them and commit the change.
# Returns the deleted user (or None if not found).
def delete_user(db: Session, user_id: int):
    user = db.query(Users).filter(Users.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user