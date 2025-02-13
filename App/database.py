from typing import Dict, Optional
from .models import Book

class BookDB:
    def __init__(self):
        self.books: Dict[int, Book] = {
            1: Book(id=1, title="The Great Gatsby", author="F. Scott Fitzgerald", price=9.99),
            2: Book(id=2, title="1984", author="George Orwell", price=10.99),
            3: Book(id=3, title="To Kill a Mockingbird", author="Harper Lee", price=12.99),
        }
    
    def get_book(self, book_id: int) -> Optional[Book]:
        return self.books.get(book_id)