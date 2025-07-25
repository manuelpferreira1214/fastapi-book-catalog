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

## Contributing

All commits must be signed (`git commit -s`).
