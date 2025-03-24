import allure
import requests
from config import BASE_URL


class TestLoginCourier:

    @allure.title('Тест логина для существующего курьера')
    @allure.description('Проверяется, что курьер может успешно авторизоваться при корректных данных.')
    @allure.step('Авторизация курьера с существующими данными')
    def test_login_existing_courier(self, register):
        login, password = register

        auth_response = requests.post(f"{BASE_URL}/courier/login", json={"login": login, "password": password})
        assert auth_response.status_code == 200
        assert "id" in auth_response.json()

    @allure.title('Тест логина для несуществующего курьера')
    @allure.description('Проверяется, что попытка логина с несуществующими данными возвращает ошибку 404.')
    @allure.step('Попытка логина с несуществующими данными')
    def test_login_not_existing_courier(self):
        fake_login = "nonexistent_user"
        fake_password = "wrong_password"

        auth_response = requests.post(f"{BASE_URL}/courier/login",
                                      json={"login": fake_login, "password": fake_password})

        assert auth_response.status_code == 404

    @allure.title('Тест логина без логина')
    @allure.description('Проверяется, что если не указан логин, возвращается ошибка 400.')
    @allure.step('Попытка логина без логина')
    def test_login_without_login(self, register):
        _, password= register


        auth_response = requests.post(f"{BASE_URL}/courier/login", json={"password": password})

        assert auth_response.status_code == 400

    @allure.title('Тест логина без пароля')
    @allure.description('Проверяется, что если не указан пароль, возвращается ошибка 400.')
    @allure.step('Попытка логина без пароля')
    def test_login_without_password(self, register):
        login, _= register

        auth_response = requests.post(f"{BASE_URL}/courier/login", json={"login": login})

        assert auth_response.status_code == 400
