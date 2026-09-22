from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

# Create FastAPI application with 3 endpoints
app = FastAPI(title="Library API")


class BookRequest(BaseModel):
    title: str
    author: str
    publication_year: int

# GET /
# Returns a message confirming that API is running.


@app.get("/")
def read_root():
    return {"message": "Library API is running"}


# POST /books/
# Accepts validated book data and return it with HTTP status 201.
@app.post("/books/", status_code=status.HTTP_201_CREATED)
def create_book(book: BookRequest):
    return book

# GET /books/{book_id}
# Returns a mock book when the ID is between 1 and 10.


@app.get("/books/{book_id}")
def get_book(book_id: int):
    if 1 <= book_id <= 10:
        return {
            "id": book_id,
            "title": "Mock Book",
            "author": "Mock Author",
            "publication_year": 2020,
        }

    # Return 404 for IDs outside the accepted range.
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found",
    )
