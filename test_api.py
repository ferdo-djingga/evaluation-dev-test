from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_review_endpoint():
    # Valid string as reviewer name, rating between 1 and 5.
    response = client.post(
        "/books/1/reviews/",
        json={
            "reviewer_name": "Fernando",
            "rating": 2,
        },
    )

    assert response.status_code == 200
