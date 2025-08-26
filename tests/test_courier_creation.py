import pytest
import requests
import allure
from utils.helpers import BASE_URL

@allure.feature("Создание курьера")
class TestCourierCreation:
    
    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self, random_courier_data, setup_courier):
        """Проверка успешного создания курьера"""
        payload = random_courier_data
        
        response = requests.post(f"{BASE_URL}/courier", json=payload)
        
        assert response.status_code == 201
        assert response.json()["ok"] == True
    
    
    @allure.title("Создание курьера без обязательного поля")
    @pytest.mark.parametrize("missing_field", ["login", "password", "firstName"])
    def test_create_courier_missing_field(self, random_courier_data, missing_field):
        """Проверка ошибки при отсутствии обязательного поля"""
        payload = random_courier_data.copy()
        payload.pop(missing_field)
        
        response = requests.post(f"{BASE_URL}/courier", json=payload)
        
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"
    
    @allure.title("Создание курьера с существующим логином")
    def test_create_courier_duplicate_login(self, setup_courier):
        """Проверка ошибки при создании курьера с существующим логином"""
        payload = {
            "login": setup_courier["login"],
            "password": "different_password",
            "firstName": "DifferentName"
        }
        
        response = requests.post(f"{BASE_URL}/courier", json=payload)
        
        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."
