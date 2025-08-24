import pytest
import requests
import allure
from utils.helpers import BASE_URL

@allure.feature("Создание заказа")
class TestOrderCreation:
    
    @allure.title("Создание заказа с разными вариантами цвета")
    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    def test_create_order_with_different_colors(self, color):
        """Проверка создания заказа с разными вариантами цвета"""
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+79991234567",
            "rentTime": 5,
            "deliveryDate": "2024-06-06",
            "comment": "Saske, come back to Konoha",
            "color": color
        }
        
        response = requests.post(f"{BASE_URL}/orders", json=payload)
        
        assert response.status_code == 201
        assert "track" in response.json()
    
    @allure.title("Создание заказа без необязательных полей")
    def test_create_order_without_optional_fields(self):
        """Проверка создания заказа без необязательных полей"""
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+79991234567",
            "rentTime": 5,
            "deliveryDate": "2024-06-06"
            # color и comment отсутствуют
        }
        
        response = requests.post(f"{BASE_URL}/orders", json=payload)
        
        assert response.status_code == 201
        assert "track" in response.json()
