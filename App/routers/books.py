from fastapi import APIRouter, HTTPException
from ..database import BookDB
from ..models import Book

router = APIRouter()
db = BookDB()

@router.get("/api/v1/books/{book_id}", response_model=Book)
async def get_book(book_id: int):
    book = db.get_book(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book