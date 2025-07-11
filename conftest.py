import pytest
from selenium import webdriver
import random


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://qa-desk.stand.praktikum-services.ru")
    yield driver 

@pytest.fixture
def registration_data():
    return {
        "email": f"testuser_{random.randint(1, 10000)}@example.com",
        "password": "TestPass123",
        "confirm_password": "TestPass123"
    }

@pytest.fixture
def registration_data_wrong_email():
    return {
        "email": f"testuser_{random.randint(1, 10000)}"
    }

@pytest.fixture
def existing_user():
    return {
        "email": f"kbsdvb@test.com",
        "password": "123456",
        "confirm_password": "123456"
    }
    
    
@pytest.fixture
def create_ad():
    return {
        "name": "новый товар",
        "description": "очень новый товар, самый лучший",
        "cost": "12345"
    }