from fastapi.testclient import TestClient
import sys
from unittest.mock import MagicMock

sys.modules['databases'] = MagicMock()
sys.modules['ormar'] = MagicMock()
sys.modules['asyncpg'] = MagicMock()

from app.main import app

client = TestClient(app)


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
