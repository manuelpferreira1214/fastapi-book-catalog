from typing import Dict

from pydantic import BaseModel

from project.models.book import Book


class BookListResponse(BaseModel):
    books: Dict[str, Book]
