import yaml
import logging
from typing import Dict
from pydantic import ValidationError
from project.models.book import Book
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s %(name)s: %(message)s"
)
logger = logging.getLogger(__name__)

def book_loader() -> Dict[str,Book]:
    loaded_books = {}
    DATA_PATH = Path(__file__).parent.parent / "data" / "books.yaml"
    try:
        with open(DATA_PATH, "r") as books:
            try:
                data = yaml.safe_load(books)
            except yaml.YAMLError as error:
                logger.error(f"Failed to read YAML file: {error}.")
                return {}
            for book in data["books"]:
                try:
                    loaded_books[book.get("isbn")] = Book(**book)
                except ValidationError as error:
                    logger.warning(f"Invalid book data for ISBN {book.get('isbn')}: {error}")
    except FileNotFoundError: 
        logger.error("'books.yaml' not found.")

    return loaded_books
