from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app
from utils.database import Base
from dependencies import get_db, get_token_header


def override_get_token_header():
    return True


app.dependency_overrides[get_token_header] = override_get_token_header

client = TestClient(app)


def test_get_frequencies():
    response = client.get("/v1/schedules/frequencies")
    assert response.status_code == 200


def test_get_references_404():
    response = client.get("/v1/schedules/references/")
    assert response.status_code == 404
