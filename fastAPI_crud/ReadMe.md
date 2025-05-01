- main.py: like your front desk — people go here first

- database.py: the plumbing — connects to the warehouse (MySQL)

- models.py: defines what a "Product" or "User" is in the warehouse

- schemas.py: defines what info clients are allowed to send/receive

- crud.py: manages stock — adds, removes, updates items in the warehouse


- Why You Need schemas.py (Pydantic Models)

| Reason | Explanation |
|--------|-------------|
| **1. Validates Incoming Data** | When someone sends a `POST` request, Pydantic ensures the data (types, structure) is correct. |
| **2. Controls Output Format** | You decide what data to return (e.g., don’t expose passwords, internal fields, etc). |
| **3. Cleaner Code & Separation** | Keeps your app clean by separating DB logic (`models.py`) from API logic. |
| **4. Required by FastAPI** | FastAPI depends on Pydantic models to parse and return data properly. |