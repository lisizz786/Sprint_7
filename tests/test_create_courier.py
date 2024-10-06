import allure
import requests
from handle import Handle
from urls import Urls
from src import register_new_courier as gen
from src import register_new_courier_without_login as gen_without_login
from src import register_new_courier_without_login as gen_without_password
from data import Users


class TestCreateCourier:
    data = gen()

    @allure.title('Создание курьера')
    def test_create_courier(self):
        response_body = '{"ok":true}'
        response = requests.post(
            f'{Urls.URL}{Handle.CREATE_COURIER}',
            TestCreateCourier.data)
        assert response.status_code == 201 and response.text == response_body

    @allure.title('Создание двух одинаковых курьеров')
    def test_courier_was_created(self):
        response = requests.post(
            f'{Urls.URL}{Handle.CREATE_COURIER}',
            TestCreateCourier.data)
        assert response.status_code == 409 and 'Этот логин уже используется' in response.text

    @allure.title('Создание курьера без логина')
    def test_create_courier_without_login(self):
        response = requests.post(
            f'{Urls.URL}{Handle.CREATE_COURIER}',
            gen_without_login())
        assert response.status_code == 400 and 'Недостаточно данных для создания учетной записи' in response.text

    @allure.title('Создание курьера без пароля')
    def test_create_courier_without_password(self):
        response = requests.post(
            f'{Urls.URL}{Handle.CREATE_COURIER}',
            gen_without_password())
        assert response.status_code == 400 and 'Недостаточно данных для создания учетной записи' in response.text

    @allure.title('Создание курьера с логином, который уже существует')
    def test_create_courier_with_existing_login(self):
        response = requests.post(
            f'{Urls.URL}{Handle.CREATE_COURIER}',
            Users.data_current)
        assert response.status_code == 409 and 'Этот логин уже используется' in response.text
