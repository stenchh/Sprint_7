import allure
import requests
from config import BASE_URL


class TestShowListOfOrders:

    @allure.title('Тест получения количества заказов для существующего курьера')
    @allure.description('Проверяется, что для авторизованного курьера возвращается корректное количество заказов.')
    @allure.step('Авторизация курьера и получение количества заказов')
    def test_get_orders_count_courier_exists(self, register):
        login, password, _ = register

        auth_response = requests.post(f"{BASE_URL}/courier/login", json={"login": login, "password": password})

        assert auth_response.status_code == 200
        auth_data = auth_response.json()

        courier_id = auth_data.get("id")
        assert courier_id is not None


        orders_count_response = requests.get(f"{BASE_URL}/api/v1/courier/{courier_id}/ordersCount")

        assert orders_count_response.status_code == 200
        response_data = orders_count_response.json()
        assert "id" in response_data and "ordersCount" in response_data


    @allure.title('Тест получения количества заказов для несуществующего курьера')
    @allure.description('Проверяется, что для несуществующего курьера возвращается ошибка 404.')
    @allure.step('Запрос количества заказов для несуществующего курьера')
    def test_show_list_of_orders_courier_nonexistent(self):
        nonexistent_courier_id = "000000000000"
        orders_count_response = requests.get(f"{BASE_URL}/api/v1/courier/{nonexistent_courier_id}/ordersCount")


        assert orders_count_response.status_code == 404
        response_data = orders_count_response.json()
        expected_message = "Курьер не найден"
        assert response_data["message"] == expected_message

    @allure.title('Тест получения количества заказов без ввода номера курьера')
    @allure.description('Проверяется, что для несуществующего курьера возвращается ошибка 404.')
    @allure.step('Запрос количества заказов для несуществующего курьера')
    def test_show_list_of_orders_empty_id(self):
        empty_courier_id = None
        orders_count_response = requests.get(f"{BASE_URL}/api/v1/courier/{empty_courier_id}/ordersCount")

        assert orders_count_response.status_code == 400
        response_data = orders_count_response.json()
        expected_message = "Недостаточно данных для поиска"
        assert response_data["message"] == expected_message

