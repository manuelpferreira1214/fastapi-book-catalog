from typing import Dict

from project.models.book import Book
from project.services.book_loader import book_loader

books = book_loader()


def get_all_books() -> Dict[str, Book]:
    return books


def get_book_by_isbn(find_isbn: str) -> Book:
    return books[find_isbn]


def get_books_by_author(find_author: str) -> Dict[str, Book]:
    author_books = {}
    for isbn, book in books.items():
        if book.author.lower() == find_author.lower():
            author_books[isbn] = book
    return author_books
