from fastapi import FastAPI
from models import TODO


app = FastAPI()

# fake db
todos = []

@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI CRUD!"}

# CREATE -  To add new to-do items, we will use the POST method.
@app.post("/todos/")
async def create_todo(todo:TODO):
    todos.append(todo)
    return todo

# READ - We’ll implement a GET method to retrieve the list of to-do items.
@app.get("/todos/")
async def get_todos():
    return todos

# To retrieve a specific item by ID, add the following route:
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"error" : "TO-DO with {todo_id} item not found"}

# UPDATE - For updating existing items, we use the PUT method. Here’s the route for updating a to-do item:
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] == update_todo
            return update_todo
    return {"error" : "TO-DO item with {todo_id} not found"}

# DELETE - Finally, to delete an item, we’ll use the DELETE method:
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {"message": "To-do item deleted!"}
    return {"error": "To-do item not found!"}
