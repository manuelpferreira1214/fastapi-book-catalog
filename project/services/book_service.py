from project.models.book import Book
from typing import Dict
from typing import List
from project.services.book_loader import book_loader

books = book_loader()

def get_all_books() -> Dict:
    return books

def get_book_by_isbn(find_isbn: str) -> Book:
    return books[find_isbn]

def get_books_by_author(find_author: str) -> List[Book]:
    author_books = []
    for book in books.values():
        if book.author.lower() == find_author.lower():
            author_books.append(book)
    return author_books
