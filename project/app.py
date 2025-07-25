from fastapi import FastAPI
from project.endpoints import books

app = FastAPI()
app.include_router(books.router)
