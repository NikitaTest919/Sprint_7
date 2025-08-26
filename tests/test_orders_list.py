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
        
        # Проверяем, что список заказов не пустой
        orders = response.json()["orders"]
        assert len(orders) > 0, "Список заказов пуст, тест не может быть выполнен"

        # Проверяем структуру первого заказа
        order = orders[0]
        assert "id" in order, "Отсутствует поле 'id' в заказе"
        assert "track" in order, "Отсутствует поле 'track' в заказе"
        assert "firstName" in order, "Отсутствует поле 'firstName' в заказе"
