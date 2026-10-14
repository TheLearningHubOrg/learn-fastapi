import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "version" in data
    assert "timestamp" in data

def test_get_items():
    response = client.get("/api/v1/items")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 2

def test_create_and_get_item():
    new_item = {
        "title": "Async SQLAlchemy 2.0",
        "description": "Database concurrency pattern",
        "price": 39.99,
        "is_active": True
    }
    create_res = client.post("/api/v1/items", json=new_item)
    assert create_res.status_code == 201
    created_data = create_res.json()
    assert created_data["title"] == new_item["title"]
    assert "id" in created_data

    item_id = created_data["id"]
    get_res = client.get(f"/api/v1/items/{item_id}")
    assert get_res.status_code == 200
    assert get_res.json()["id"] == item_id

def test_get_item_not_found():
    response = client.get("/api/v1/items/999999")
    assert response.status_code == 404
