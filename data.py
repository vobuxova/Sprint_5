import random


    
def get_registration_data():
    return {
        "email": f"testuser_{random.randint(1, 10000)}@example.com",
        "password": "TestPass123",
        "confirm_password": "TestPass123"
    }

def get_registration_data_wrong_email():
    return {
        "email": f"testuser_{random.randint(1, 10000)}"
    }

def get_existing_user():
    return {
        "email": "kbsdvb@test.com",
        "password": "123456",
        "confirm_password": "123456"
    }

def get_create_ad_data():
    return {
        "name": "новый товар",
        "description": "очень новый товар, самый лучший",
        "cost": "12345"
    }