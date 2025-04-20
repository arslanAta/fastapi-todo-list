import uvicorn
from fastapi import FastAPI,HTTPException
from pydantic import  BaseModel

app = FastAPI()


class NewBook(BaseModel):
    title:str
    author:str

books = [
    {
        "id":1,
        "name":"My book1",
        "author":'Someone1'
    },
    {
        "id":2,
        "name":"My book2",
        "author":'Someone2'
    }
]

@app.get('/books',tags=['Books'],summary="Get all books")
def root():
    return books

@app.get("/books/{book_id}",tags=['Books'],summary="Get book by id")
def get_book(book_id:int):
    for book in books:
        if book['id'] == book_id:
            return book
    raise  HTTPException(status_code=404)

@app.post('/books',tags=['Books'])
def add_book(new_book:NewBook):
    books.append({
        "id":len(books)+1,
        "title":new_book.title,
        "author":new_book.author
    })
    return books

if __name__ == "__main__":
    uvicorn.run("main:app",reload=True)