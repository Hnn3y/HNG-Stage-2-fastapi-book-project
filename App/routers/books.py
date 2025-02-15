from fastapi import APIRouter, HTTPException
from typing import List
from app.models.book import Book
from app.database.books import get_book_by_id, get_all_books

router = APIRouter(
    prefix="/api/v1/books",
    tags=["books"]
)

@router.get("/{book_id}", response_model=Book)
async def get_book(book_id: int):
    book = await get_book_by_id(book_id)
    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )
    return book

@router.get("/", response_model=List[Book])
async def list_books():
    return await get_all_books()