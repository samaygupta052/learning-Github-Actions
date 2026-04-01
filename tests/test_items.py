from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "FastAPI is running"}

def test_create_item():
    response = client.post("/items/", json={
        "name": "Laptop",
        "price": 50000,
        "is_available": True
    })
    assert response.status_code == 200
    assert response.json()["message"] == "Item added"

def test_get_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_item_success():
    response = client.get("/items/0")
    assert response.status_code == 200

def test_get_item_not_found():
    response = client.get("/items/999")
    assert response.status_code == 404