# Purpose: This imports the create_engine function from SQLAlchemy.

# What it does: It creates a connection engine to your MySQL database. This is your primary interface to the database and is used by SQLAlchemy to issue SQL commands.
from sqlalchemy import create_engine

# Purpose: Imports the declarative_base function.

# What it does: This function returns a base class which your ORM models (i.e., table representations in Python) will inherit from.

# Think of it like this: Base = declarative_base() is saying “Hey SQLAlchemy, I’m about to define models, and I want them to be recognized as database tables.”
from sqlalchemy.ext.declarative import declarative_base

# Purpose: Imports the sessionmaker function from SQLAlchemy.

# What it does: This is a factory for creating database sessions. Sessions manage the conversation between your Python code and the database (you use sessions to query, add, update, and delete data).
from sqlalchemy.orm import sessionmaker

# Replace with your actual MySQL credentials
DATABASE_URL = "mysql+pymysql://drashti:Drashti%4011@localhost:3306/dbname"

# What it does: Creates an SQLAlchemy engine that will be used to connect to the MySQL database.
engine = create_engine(DATABASE_URL)

# What it does: Creates a session factory (SessionLocal) that is used to make actual database session instances.

# autoflush=False: Prevents SQLAlchemy from automatically flushing pending changes to the database (you manually commit them).

# autocommit=False: You have to manually call .commit() on the session to persist changes.

# bind=engine: Binds the session to the database engine we just created.
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

# What it does: Creates a base class (Base) for all your SQLAlchemy models.

# Any model you define like this:
# class User(Base):
#     __tablename__ = "users"
Base = declarative_base()


# engine → Connects SQLAlchemy to your MySQL database.

# SessionLocal → Used to talk to the database in your routes.

# Base → Used to define models that map to tables in your DB.

# DATABASE_URL → Holds your database credentials and path.