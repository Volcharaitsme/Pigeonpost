from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "PigeonPost" in response.json()["message"]

def test_create_and_get_pigeon():
    # Создаем голубя
    response = client.post("/api/v1/pigeons", json={"name": "Геннадий", "speed_kmh": 65})
    assert response.status_code == 200
    data = response.json()
    pigeon_id = data["id"]
    assert data["name"] == "Геннадий"
    
    # Получаем его
    response = client.get(f"/api/v1/pigeons/{pigeon_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Геннадий"

def test_pigeon_not_found():
    response = client.get("/api/v1/pigeons/9999")
    assert response.status_code == 404