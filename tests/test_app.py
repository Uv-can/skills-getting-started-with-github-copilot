import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_list_activities():
    # Arrange: (No setup needed for in-memory default)
    # Act
    response = client.get("/activities")
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert len(data) > 0
    for activity in data.values():
        assert "description" in activity
        assert "participants" in activity
        assert isinstance(activity["participants"], list)

def test_signup_for_activity():
    # Arrange
    activity_name = list(client.get("/activities").json().keys())[0]
    email = "testuser@mergington.edu"
    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    # Assert
    assert response.status_code == 200
    assert f"Signed up {email}" in response.json()["message"]
    # Confirm participant is added
    participants = client.get("/activities").json()[activity_name]["participants"]
    assert email in participants

def test_prevent_duplicate_signup():
    # Arrange
    activity_name = list(client.get("/activities").json().keys())[0]
    email = "dupeuser@mergington.edu"
    client.post(f"/activities/{activity_name}/signup?email={email}")
    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    # Assert
    assert response.status_code == 400 or response.status_code == 409
    assert "already signed up for this activity" in response.json()["detail"].lower()
