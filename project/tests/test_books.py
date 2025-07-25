import pytest
from fastapi.testclient import TestClient
from project.app import app
from project.services.book_loader import book_loader
from project.models.book import Book
from datetime import date

client = TestClient(app)
books = book_loader()

def test_list_books():
    response = client.get("/books")
    assert isinstance(response.json(), dict)

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
    response = client.get(f"/books/{isbn}").json()
    assert response["isbn"] == isbn
    assert response["title"] == expected_title

@pytest.mark.parametrize("isbn", [
    "1234567891234",
    "0000000000000",
])
def test_get_book_error_404(isbn):
    isbn = "1234567891234"
    response = client.get(f"/books/{isbn}").json()
    assert response["detail"] == "Book not found."
