from pydantic import BaseModel,Field
from typing import  List,Optional
from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

class AddTodoSchema(BaseModel):
    text: str = Field(max_length=150)

class TodoSchema(AddTodoSchema):
    id: int


todos:Optional[List[TodoSchema]] = []

@app.get('/todos',tags=['Todo management'])
def get_todos():
    return todos

@app.get('/todos/{todo_id}',tags=['Todo management'])
def get_todo_by_id(todo_id:int):
    for todo in todos:
        if todo.id == todo_id :
            return todo
    raise HTTPException(status_code=404)


@app.post('/todos',tags=['Todo management'])
def add_todo(new_todo:AddTodoSchema):
    todo = TodoSchema(
        id=len(todos) + 1,
        text=new_todo.text
    )
    todos.append(todo)
    return todos

@app.patch('/todos/{todo_id}',tags=['Todo management'])
def update_todo(todo_id:int,updated_todo:AddTodoSchema):
    for todo in todos:
        if todo.id == todo_id:
            todo.text = updated_todo.text
            return todo
    raise HTTPException(status_code=404)

@app.delete('/todos/{todo_id}',tags=['Todo management'])
def delete_todo(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return todos
    raise HTTPException(status_code=404)


if __name__ == "__main__":
    uvicorn.run("main:app",reload=True)