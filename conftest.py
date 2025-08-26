import pytest
import requests
import random
import string
from utils.helpers import BASE_URL

def generate_random_string(length):
    """Генерирует случайную строку из букв нижнего регистра"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def register_new_courier():
    """Регистрирует нового курьера и возвращает данные"""
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    
    response = requests.post(f"{BASE_URL}/courier", json=payload)
    
    if response.status_code == 201:
        return {
            "login": login,
            "password": password,
            "first_name": first_name
        }
    return None

def delete_courier(courier_id):
    """Удаляет курьера по ID"""
    requests.delete(f"{BASE_URL}/courier/{courier_id}")

def login_courier(login, password):
    """Авторизует курьера и возвращает ID"""
    payload = {"login": login, "password": password}
    response = requests.post(f"{BASE_URL}/courier/login", json=payload)
    
    if response.status_code == 200:
        return response.json()["id"]
    return None

@pytest.fixture
def setup_courier():
    """Фикстура для создания и удаления тестового курьера"""
    courier_data = register_new_courier()
    yield courier_data
    
    # Удаление после теста
    if courier_data:
        courier_id = login_courier(courier_data["login"], courier_data["password"])
        if courier_id:
            delete_courier(courier_id)

@pytest.fixture
def random_courier_data():
    """Фикстура для генерации случайных данных курьера"""
    return {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstName": generate_random_string(10)
    }
