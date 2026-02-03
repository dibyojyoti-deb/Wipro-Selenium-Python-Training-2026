import requests
import pytest

BASE_URL = "http://127.0.0.1:5000/api"

def test_get_all_movies():
    response = requests.get(f"{BASE_URL}/movies")
    assert response.status_code == 200
    assert len(response.json()) >= 1

def test_add_movie():
    payload = {
        "movie_name": "The Dark Knight",
        "language": "English",
        "duration": "2h 32m",
        "price": 300
    }
    response = requests.post(f"{BASE_URL}/movies", json=payload)
    assert response.status_code == 201
    assert response.json()["movie_name"] == "The Dark Knight"

def test_book_ticket_success():
    payload = {"movie_id": 101, "seats": 2}
    response = requests.post(f"{BASE_URL}/bookings", json=payload)
    assert response.status_code == 201
    assert "total_price" in response.json()

def test_book_ticket_invalid_movie():
    payload = {"movie_id": 999, "seats": 2}
    response = requests.post(f"{BASE_URL}/bookings", json=payload)
    assert response.status_code == 400