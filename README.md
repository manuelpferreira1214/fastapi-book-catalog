# FastAPI Book Catalog

Simple book catalog service that reads from a static YAML file and exposes a REST API using FastAPI and Pydantic.

---

## Prerequisites

* Python 3.12
* Poetry installed
* Git installed and Github account
* Docker installed

---

## Development Setup

1. Clone the repository

   ```bash
   git clone https://github.com/username/fastapi-book-catalog.git
   ```

2. Change to the project directory

   ```bash
   cd fastapi-book-catalog
   ```

3. Install dependencies with Poetry

   ```bash
   poetry install
   ```

4. Activate virtual environment

   ```bash
   poetry shell
   ```

### Additonal note

To activate the virtual environment manually:

```bash
source $(poetry env info --path)/bin/activate
```

---

## API Endpoints

### List all books

* **GET** `/books`

  Returns all books in the catalog as a Dictionary of Book instances.

### Filter books by author

* **GET** `/books?author=AUTHOR_NAME`

  Returns books by the specified author.

  * **Query parameters:**

    * `author` (optional): Name of the author to filter books by.
  * **Example request:**

    ```bash
    curl -X GET "http://localhost:8000/books?author=Homer"
    ```

  * **Expected response:**

    ```json
    {
      "9780140449112": {
        "title": "The Iliad",
        "author": "Homer",
        "published_date": "1998-11-01"
      },
      "9780140449273": {
         "title": "The Odyssey",
         "author": "Homer",
         "published_date": "1999-10-01"
      }
    }  
    ```

### Filter books by ISBN

* **GET** `/books/isbn/ISBN_NUMBER`

  Returns the book that matches the specified ISBN.

  * **Example request:**

    ```bash
    curl -X GET "http://localhost:8000/books/isbn/9780140449112"
    ```

  * **Expected response:**

    ```json
    {
      "9780140449112": {
        "title": "The Iliad",
        "author": "Homer",
        "published_date": "1998-11-01"
      }
    }
    ```

---

## Contributing

All commits must be signed (`git commit -s`).
