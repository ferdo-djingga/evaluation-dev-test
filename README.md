# Evaluation Dev Test

Junior Software Engineer Day 1 Assignment

## Install Dependencies

Install the Poetry dependencies:

```bash
poetry install --no-root
```

## PostgreSQL Setup

Start PostgreSQL and create the database:

```bash
brew services start postgresql
createdb library_db
```

Run the database script:

```bash
poetry run python db_operations.py
```

## MongoDB Setup

Start MongoDB:

```bash
brew services start mongodb-community
```

## Run the FastAPI App

```bash
poetry run uvicorn main:app --reload
```

Open the Swagger UI:

```text
http://127.0.0.1:8000/docs
```

Stop the server.

## Run Tests

Make sure MongoDB is running, then run:

```bash
poetry run pytest -v
```

## Other Script

Run the GitHub user fetcher:

```bash
poetry run python github_fetcher.py
```

## Screenshots

### GitHub Pull Request

![GitHub pull request](screenshots/Task1_Github_PR.png)

### PostgreSQL Output

![PostgreSQL output](screenshots/Task2_PostgreSQL_Output.png)

### FastAPI Swagger Tests

![GET root returning 200](screenshots/Task3_GET_root_200.png)

![POST book returning 201](screenshots/Task3_POST_books_201.png)

![GET valid book returning 200](screenshots/Task3_GET_book_valid_200.png)

![GET invalid book returning 404](screenshots/Task3_GET_book_invalid_404.png)

![POST review returning 200](screenshots/Task4_POST_reviews_200.png)