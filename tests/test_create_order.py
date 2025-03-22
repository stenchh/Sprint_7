import requests

BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1'
class TestCreateOrder:
    @pytest.mark.parametrize("color_param, expected_status", TEST_DATA)
    def test_create_order_with_colors(color_param, expected_status):
        request_body = {**ORDER_BODY, **color_param} if color_param else ORDER_BODY.copy()

        if not color_param:
            request_body.pop("color", None)

        response = requests.post(f"{BASE_URL}/orders", json=request_body)

        assert response.status_code == expected_status

        response_data = response.json()
        assert "track" in response_data
