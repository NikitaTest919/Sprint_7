import pytest
import requests
import allure
from utils.helpers import BASE_URL

@allure.feature("Авторизация курьера")
class TestCourierLogin:
    
    @allure.title("Успешная авторизация курьера")
    def test_login_courier_success(self, setup_courier):
        """Проверка успешной авторизации курьера"""
        payload = {
            "login": setup_courier["login"],
            "password": setup_courier["password"]
        }
        
        response = requests.post(f"{BASE_URL}/courier/login", json=payload)
        
        assert response.status_code == 200
        assert "id" in response.json()
    
    @allure.title("Авторизация без обязательного поля")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_courier_missing_field(self, missing_field):
        """Проверка ошибки при отсутствии обязательного поля"""
        payload = {"login": "test", "password": "123456"}
        payload.pop(missing_field)
        
        response = requests.post(f"{BASE_URL}/courier/login", json=payload)
        
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"
    
    @allure.title("Авторизация с неверными данными")
    def test_login_courier_invalid_credentials(self, setup_courier):
        """Проверка ошибки при неверных учетных данных"""
        payload = {
            "login": setup_courier["login"],
            "password": "wrong_password"
        }
        
        response = requests.post(f"{BASE_URL}/courier/login", json=payload)
        
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"
    
    @allure.title("Авторизация несуществующего курьера")
    def test_login_nonexistent_courier(self):
        """Проверка ошибки при авторизации несуществующего курьера"""
        payload = {
            "login": "nonexistent_user",
            "password": "password123"
        }
        
        response = requests.post(f"{BASE_URL}/courier/login", json=payload)
        
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"
