import pytest
from fastapi.testclient import TestClient
from random import randint
from app.main import app


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c

def test_when_app_runing_status_endpoint_should_return_OK(client):
    response = client.get("/status")
    assert response.status_code == 200
    data = response.json()
    assert data["Message"] == "OK"


def test_when_given_user_name_should_create_a_student_in_db(client):

    random = randint(0,100000)
    first_name = f"Jhon {random}"
    last_name = f"World {random}"
    create_response = client.post("/student/", json={"first_name":first_name, "last_name":last_name})
    assert create_response.status_code == 200
    student_id = create_response.json()["id"]
    assert student_id != None


