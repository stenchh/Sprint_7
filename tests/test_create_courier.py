import requests
class TestCreateCourier:

    def test_create_courier_with_full_data(register):
        assert len(register) == 3

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', json={
            "login": register[0],
            "password": register[1],
            "firstName": register[2]
        })
        assert response.status_code == 201

        assert response.json() == {"ok": True}

    def test_create_courier_without_login():
        payload = {
            "login": '',
            "password": 'ninja1',
            "firstName": 'ninja'
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        assert response.status_code == 400
        assert response.json() == {"message": "Недостаточно данных для создания учетной записи"}

    def test_create_courier_without_password():
        payload = {
            "login": 'ninini',
            "password": '',
            "firstName": 'ninja'
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        assert response.status_code == 400
        assert response.json() == {"message": "Недостаточно данных для создания учетной записи"}

    def test_duplicate_courier_409():
        payload = {
            "login": "ninja",
            "password": "ninja1",
            "firstName": "naruto"
        }

        create_response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        assert create_response.status_code == 201
        assert create_response.json() == {"ok": True}

        duplicate_response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        assert duplicate_response.status_code == 409
        assert duplicate_response.json() == {"message": "Этот логин уже используется"}




