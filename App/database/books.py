books_db = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"id": 3, "title": "1984", "author": "George Orwell", "year": 1949}
]

async def get_book_by_id(book_id: int):
    return next((book for book in books_db if book["id"] == book_id), None)

async def get_all_books():
    return books_db