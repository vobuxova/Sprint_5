from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from Sprint_5.locators import Locators
from Sprint_5.data import get_existing_user

class TestLoginUser:
    
    def test_login_user(self, driver):
    
        WebDriverWait(driver, 10).until(
           EC.element_to_be_clickable(Locators.LOGIN_REG_BUTTON)
        ).click()
        
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(get_existing_user()["email"])
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(get_existing_user()["password"])
      
    
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        
        assert 'https://qa-desk.stand.praktikum-services.ru/login' in driver.current_url
    
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.AVATAR))
    
        user_name = driver.find_element(*Locators.USER_NAME)
        assert user_name.text == 'User.'
        
