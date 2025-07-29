import logging
from fastapi import APIRouter
from fastapi import HTTPException
from project.services.book_loader import book_loader
from project.models.book import Book

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s %(name)s: %(message)s"
)
logger = logging.getLogger(__name__)

router = APIRouter()
books = book_loader()

@router.get("/books")
def get_books():
    return books

@router.get("/books/{isbn}")
def find_book_by_isbn(isbn: str) -> Book:
    try:
        return books[isbn]
    except KeyError:
        logger.warning(f"Book with ISBN {isbn} not found.")
        raise HTTPException(status_code=404, detail="Book not found.") 
