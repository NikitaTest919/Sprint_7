import pytest
import requests
import allure
from utils.helpers import BASE_URL

@allure.feature("Список заказов")
class TestOrdersList:
    
    @allure.title("Получение списка заказов")
    def test_get_orders_list(self):
        """Проверка получения списка заказов"""
        response = requests.get(f"{BASE_URL}/orders")
        
        assert response.status_code == 200
        assert isinstance(response.json()["orders"], list)
        
        # Проверяем структуру первого заказа, если список не пустой
        if response.json()["orders"]:
            order = response.json()["orders"][0]
            assert "id" in order
            assert "track" in order
            assert "firstName" in order
