from project.models.book import Book
from pydantic import BaseModel
from typing import Dict

class BookListResponse(BaseModel):
    books: Dict[str, Book]
