import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200

def test_create_order():
    response = client.post("/api/orders", json={"product_id": 1, "quantity": 2})
    assert response.status_code == 201
    assert response.json()["status"] == "pending"
