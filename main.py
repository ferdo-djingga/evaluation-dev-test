from datetime import datetime
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from pymongo import MongoClient
from pymongo.errors import PyMongoError

# Creates the FastAPI application with 4 endpoints
app = FastAPI(title="Library API")

# Connects to local MongoDB server
mongo_client = MongoClient(
    "mongodb://localhost:27017/"
)

# Selects database and collection
mongo_database = mongo_client["library_db"]
reviews_collection = mongo_database["book_reviews"]


class BookRequest(BaseModel):
    # Validates the book request data from POST /books/
    title: str
    author: str
    publication_year: int


@app.get("/")
# Returns a message confirming that API is running.
def read_root():
    return {"message": "Library API is running"}


@app.post("/books/", status_code=status.HTTP_201_CREATED)
# Accepts validated book data and return it with HTTP status 201.
def create_book(book: BookRequest):
    return book


@app.get("/books/{book_id}")
# Returns a mock book when the ID is between 1 and 10.
def get_book(book_id: int):
    if 1 <= book_id <= 10:
        return {
            "id": book_id,
            "title": "Mock Book",
            "author": "Mock Author",
            "publication_year": 2020,
        }

    # Returns 404 for IDs outside the accepted range.
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found",
    )


class ReviewRequest(BaseModel):
    # Validates the review request data from POST /books/{book_id}/reviews/
    reviewer_name: str
    rating: int = Field(ge=1, le=5)


@app.post("/books/{book_id}/reviews/")
# Creates then stores a review for a book in MongoDB
def create_review(book_id: int, review: ReviewRequest):
    review_document = {
        "book_id": book_id,
        "reviewer_name": review.reviewer_name,
        "rating": review.rating,
        "created_at": datetime.now(),
    }

    try:
        # Stores a copy in MongoDB
        # PyMongo adds an _id field to the dictionary
        reviews_collection.insert_one(review_document.copy())

    except PyMongoError as error:
        # Returns an HTTP error if MongoDB cannot save the review
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Could not save review",
        ) from error

    return review_document
