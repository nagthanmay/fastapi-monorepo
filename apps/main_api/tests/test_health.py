from fastapi.testclient import TestClient
from apps.main_api.main import app

client = TestClient(app)

def test_health():
    response = client.get("/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}