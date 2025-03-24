import allure
import requests
from config import BASE_URL
class TestCreateCourier:

    @allure.title('Тест создания курьера с полными данными')
    @allure.description('Проверяется создание курьера с корректными данными (логин, пароль, имя).')
    @allure.step('Создание курьера с полными данными')
    def test_create_courier_with_full_data(self, register):
        assert len(register) == 3
        response = requests.post(f"{BASE_URL}/courier", json={
            "login": register[0],
            "password": register[1],
            "firstName": register[2]
        })
        assert response.status_code == 201

        assert response.json() == {"ok": True}

    @allure.title('Тест создания курьера без логина')
    @allure.description('Проверяется создание курьера без логина, ожидается ошибка 400.')
    @allure.step('Создание курьера без логина')
    def test_create_courier_without_login(self):
        payload = {
            "login": '',
            "password": 'ninja1',
            "firstName": 'ninja'
        }

        response = requests.post(f"{BASE_URL}/courier", json=payload)

        assert response.status_code == 400
        response_data = response.json()
        expected_message = "Недостаточно данных для создания учетной записи"
        assert response_data["message"] == expected_message


    @allure.title('Тест создания курьера без пароля')
    @allure.description('Проверяется создание курьера без пароля, ожидается ошибка 400.')
    @allure.step('Создание курьера без пароля')
    def test_create_courier_without_password(self):
        payload = {
            "login": 'ninini',
            "password": '',
            "firstName": 'ninja'
        }

        response = requests.post(f"{BASE_URL}/courier", json=payload)

        assert response.status_code == 400
        response_data = response.json()
        expected_message = "Недостаточно данных для создания учетной записи"
        assert response_data["message"] == expected_message


    @allure.title('Тест дублирования курьера')
    @allure.description('Проверяется попытка создания курьера с уже существующим логином. Ожидается ошибка 409.')
    @allure.step('Создание курьера с уже существующим логином')
    def test_duplicate_courier_409(self):
        payload = {
            "login": "ninja",
            "password": "ninja1",
            "firstName": "naruto"
        }


        create_response = requests.post(f"{BASE_URL}/courier", json=payload)
        assert create_response.status_code == 201
        assert create_response.json() == {"ok": True}


        duplicate_response = requests.post(f"{BASE_URL}/courier", json=payload)
        assert duplicate_response.status_code == 409
        response_data = duplicate_response.json()
        expected_message = "Этот логин уже используется"
        assert response_data["message"] == expected_message
