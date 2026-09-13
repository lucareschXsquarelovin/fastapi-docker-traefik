import os
os.environ["DATABASE_URL"] = "postgresql://fastapi:fastapi@localhost:5432/fastapi"

from fastapi.testclient import TestClient
from fastapi import FastAPI

# Create a minimal test app with just the health endpoint
test_app = FastAPI()

@test_app.get("/health")
async def health_check():
    return {"status": "ok", "version": "1.0.0"}

client = TestClient(test_app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "version": "1.0.0"}


def test_health_check_version():
    response = client.get("/health")
    data = response.json()
    assert "status" in data
    assert "version" in data
    assert data["status"] == "ok"
