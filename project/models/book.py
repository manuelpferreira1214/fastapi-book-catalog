from pydantic import BaseModel
from pydantic import Field
from pydantic import field_validator
from datetime import date
import re

class Book(BaseModel):
    isbn: str = Field(...)
    title: str = Field(...)
    author: str = Field(...)
    published_date: date = Field(...)

    @field_validator("isbn", mode="after")
    def check_valid_isbn(cls, isbn: str) -> str:
        if not re.fullmatch(r"97[89]\d{10}", isbn):
            raise ValueError("Invalid ISBN. Must be a 13-digit number starting with '978' or '979'.")
        return isbn
