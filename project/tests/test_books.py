import pytest
from fastapi.testclient import TestClient
from project.app import app
from project.services.book_loader import book_loader
from project.models.book import Book
from datetime import date

client = TestClient(app)
books = book_loader()

def test_list_books():
    response = client.get("/books?author=")
    assert isinstance(response.json(), dict)

@pytest.mark.parametrize("valid_author", [
    "Jane Austen",
    "George Orwell",
    "Fyodor Dostoevsky"
])
def test_get_books_by_author(valid_author: str):
    response = client.get(f"/books?author={valid_author}")
    data = response.json()
    assert all(book["author"].lower() == valid_author.lower() for book in data.values())

@pytest.mark.parametrize("author", [
    "Manuel",
    "Rui",
])
def test_get_author_error_404(author):
    response = client.get(f"/books?author={author}").json()
    assert response["detail"] == "Author not found."

@pytest.mark.parametrize("invalid_isbn", [
    "1234567890123",
    "978123456789",
    "978123456789X"
])
def test_book_invalid_isbn_format(invalid_isbn):
    with pytest.raises(ValueError, match="Invalid ISBN"):
        Book(
            isbn=invalid_isbn,
            title="Book with invalid ISBN",
            author="Someone",
            published_date=date(2025, 7, 29)
        )

@pytest.mark.parametrize("isbn, expected_title", [
    ("9780141439518", "Pride and Prejudice"),
    ("9780452284234", "1984")
])
def test_get_book_by_isbn(isbn, expected_title):
    response = client.get(f"/books/isbn/{isbn}").json()
    assert response["isbn"] == isbn
    assert response["title"] == expected_title

@pytest.mark.parametrize("isbn", [
    "1234567891234",
    "0000000000000",
])
def test_get_book_error_404(isbn):
    response = client.get(f"/books/isbn/{isbn}").json()
    assert response["detail"] == "Book not found."
