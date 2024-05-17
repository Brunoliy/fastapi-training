from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_roo_must_return_ok_and_message():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'Message': 'Olá Mundo!'}
