import allure
import requests
from config import BASE_URL


class TestShowListOfOrders:

    @allure.title('Тест получения количества заказов для существующего курьера')
    @allure.description('Проверяется, что для авторизованного курьера возвращается корректное количество заказов.')
    @allure.step('Авторизация курьера и получение количества заказов')
    def test_get_orders_count(self, register):
        login, password  = register

        auth_response = requests.post(f"{BASE_URL}/courier/login", json={"login": login, "password": password})

        assert auth_response.status_code == 200
        auth_data = auth_response.json()

        courier_id = auth_data.get("id")
        assert courier_id is not None


        orders_count_response = requests.get(f"{BASE_URL}/api/v1/courier/{courier_id}/ordersCount")

        assert orders_count_response.status_code == 200

    @allure.title('Тест получения количества заказов для несуществующего курьера')
    @allure.description('Проверяется, что для несуществующего курьера возвращается ошибка 404.')
    @allure.step('Запрос количества заказов для несуществующего курьера')
    def test_show_list_of_orders(self):
        nonexistent_courier_id = "000000000000"
        orders_count_response = requests.get(f"{BASE_URL}/api/v1/courier/{nonexistent_courier_id}/ordersCount")


        assert orders_count_response.status_code == 404
