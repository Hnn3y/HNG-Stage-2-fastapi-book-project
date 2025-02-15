from fastapi import FastAPI, HTTPException
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI()

# Database simulation
books_db = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"id": 3, "title": "1984", "author": "George Orwell", "year": 1949}
]

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int

@app.get("/api/v1/books/{book_id}", response_model=Book)
async def get_book(book_id: int):
    book = next((book for book in books_db if book["id"] == book_id), None)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.get("/api/v1/books", response_model=List[Book])
async def get_books():
    return books_db