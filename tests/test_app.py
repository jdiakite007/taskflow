import pytest
from app.main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home_endpoint(client):
    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()

    assert data["application"] == "Taskflow"


def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"
    assert data["application"] == "taskflow"


def test_list_tasks_endpoint(client):
    response = client.get("/tasks")

    assert response.status_code == 200

    data = response.get_json()

    assert "tasks" in data
    assert len(data["tasks"]) == 2
    assert data["tasks"][0]["id"] == 1
    assert data["tasks"][0]["title"] == "Learn Git"
    assert data["tasks"][0]["completed"] is False
