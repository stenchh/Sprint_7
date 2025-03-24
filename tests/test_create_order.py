from data import DATA_COLORS, DATA_NO_COLOR, ORDER_BODY
from config import BASE_URL
import allure
import pytest
import requests
class TestCreateOrder:
    @allure.title("Тест создания заказа с цветами")
    @allure.description("Проверяется создание заказа с разными цветами и ожидаемый статус ответа.")
    @allure.step("Отправка POST-запроса для создания заказа с разными цветами")
    @pytest.mark.parametrize("color_param, expected_status", DATA_COLORS)
    def test_create_order_with_colors(self, color_param, expected_status):
        request_body = {**ORDER_BODY, **color_param}
        response = requests.post(f"{BASE_URL}/orders", json=request_body)

        assert response.status_code == expected_status
        assert "track" in response.json()

    @allure.title("Тест создания заказа без цвета")
    @allure.description("Проверяется создание заказа без указания цвета и ожидаемый статус ответа.")
    @allure.step("Отправка POST-запроса для создания заказа без цвета")
    @pytest.mark.parametrize("color_param, expected_status", DATA_NO_COLOR)
    def test_create_order_without_color(self, color_param, expected_status):
        request_body = ORDER_BODY.copy()
        request_body.pop("color", None)

        response = requests.post(f"{BASE_URL}/orders", json=request_body)

        assert response.status_code == expected_status
        assert "track" in response.json()
