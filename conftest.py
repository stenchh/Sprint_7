import pytest
import requests
from helpers import create_courier_payload

BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1"


@pytest.fixture
def register():

    payload = create_courier_payload()

    response = requests.post(f"{BASE_URL}/courier", json=payload)
    response.raise_for_status()

    yield payload["login"], payload["password"], payload["firstName"]


    login_data = {"login": payload["login"], "password": payload["password"]}
    auth_response = requests.post(f"{BASE_URL}/courier/login", json=login_data)

    if auth_response.status_code == 200 and "id" in auth_response.json():
        courier_id = auth_response.json()["id"]
        requests.delete(f"{BASE_URL}/courier/{courier_id}")
