from pydantic import BaseModel,Field
from typing import  List,Optional
from fastapi import  FastAPI
import uvicorn

app = FastAPI()

class AddTodoSchema(BaseModel):
    text: str = Field(max_length=150)

class TodoSchema(AddTodoSchema):
    id: int


todos:Optional[List[TodoSchema]] = []

@app.get('/todos')
def get_todos():
    return todos

@app.post('/todos')
def add_todo(new_todo:AddTodoSchema):
    todo = TodoSchema(
        id=len(todos) + 1 | 1,
        text=new_todo.text
    )
    todos.append(todo)
    return todos

if __name__ == "__main__":
    uvicorn.run("main:app",reload=True)