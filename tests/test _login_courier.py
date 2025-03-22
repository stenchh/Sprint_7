import requests
BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1'
class TestLoginCourier:
    def test_login_existing_courier(self):
        payload = {
            "login": 'login',
            "password": 'password1'
        }
        reg_data = {**payload, "FirstName": "name"}
        reg_response = requests.post(f"{BASE_URL}/courier", json=reg_data)
        assert reg_response.status_code == 201


        auth_response = requests.post(f"{BASE_URL}/courier/login", json=payload)
        assert auth_response.status_code == 200
        assert "id" in auth_response.json()
