import logging
from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Query
from project.services.book_loader import book_loader
from project.models.book import Book
from typing import List
from typing import Dict
from typing import Optional
from project.services.book_service import get_all_books
from project.services.book_service import get_book_by_isbn
from project.services.book_service import get_books_by_author


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s %(name)s: %(message)s"
)
logger = logging.getLogger(__name__)

router = APIRouter()
books = book_loader()

@router.get("/books")
def get_books(author: Optional[str] = Query(default=None)) -> Dict:
    if author:
        list_books = get_books_by_author(author)
        if not list_books:
            logger.warning(f"No book from {author} found.")
            raise HTTPException(status_code=404, detail="Author not found.")
        return {isbn: book for isbn, book in books.items() if book in list_books}
    return get_all_books()

@router.get("/books/isbn/{isbn}")
def find_book_by_isbn(isbn: str) -> Book:
    try:
        return get_book_by_isbn(isbn)
    except KeyError:
        logger.warning(f"Book with ISBN {isbn} not found.")
        raise HTTPException(status_code=404, detail="Book not found.") 
