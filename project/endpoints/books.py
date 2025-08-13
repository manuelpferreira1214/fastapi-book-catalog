import logging
from typing import Optional

from fastapi import APIRouter, HTTPException, Query

from project.models.book import Book
from project.models.book_list_response import BookListResponse
from project.services.book_service import get_all_books
from project.services.book_service import get_book_by_isbn
from project.services.book_service import get_books_by_author

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/books", response_model=BookListResponse)
def get_books(author: Optional[str] = Query(default=None)) -> BookListResponse:
    if author:
        list_books = get_books_by_author(author)
        if not list_books:
            logger.warning(f"No book from {author} found.")
            raise HTTPException(status_code=404, detail="Author not found.")
    else:
        list_books = get_all_books()
    return BookListResponse(books=list_books)


@router.get("/books/isbn/{isbn}")
def find_book_by_isbn(isbn: str) -> Book:
    try:
        return get_book_by_isbn(isbn)
    except KeyError:
        logger.warning(f"Book with ISBN {isbn} not found.")
        raise HTTPException(status_code=404, detail="Book not found.")
