import pytest
from fastapi.testclient import TestClient

from src.server.api import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World",
                               'link': 'http://127.0.0.1:8000/ram-data/1/'
                               }


@pytest.mark.parametrize("number", [1, 2, 3])
def test_get_n_record(number):
    response = client.get(f"ram-data/{number}/")
    assert response.status_code == 200
    assert len(response.json()) == number
