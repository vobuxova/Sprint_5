from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from Sprint_5.locators import Locators

def test_registration_new_user(driver, registration_data):

    WebDriverWait(driver, 10).until(
       EC.element_to_be_clickable(Locators.LOGIN_REG_BUTTON)
    ).click()
    
    driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()
    
    driver.find_element(*Locators.EMAIL_FIELD).send_keys(registration_data["email"])
    driver.find_element(*Locators.PASSWORD_FIELD).send_keys(registration_data["password"])
    driver.find_element(*Locators.CONFIRM_PASSWORD_FIELD).send_keys(registration_data["confirm_password"])

    driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()

    assert 'https://qa-desk.stand.praktikum-services.ru/regiatration' in driver.current_url  
    
    avatar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.AVATAR))
    assert avatar.is_displayed() is True

    user_name = driver.find_element(*Locators.USER_NAME)
    assert user_name.text == 'User.'
     

    driver.quit() 


def test_registration_with_wrong_email(driver, registration_data_wrong_email):
    
    WebDriverWait(driver, 10).until(
       EC.element_to_be_clickable(Locators.LOGIN_REG_BUTTON)
    ).click()
    
    driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()
    
    driver.find_element(*Locators.EMAIL_FIELD).send_keys(registration_data_wrong_email["email"])
    

    driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()
    
    WebDriverWait(driver, 10).until(
         EC.presence_of_all_elements_located(Locators.BORDER_EMAIL)
    )
    elements = driver.find_elements(*Locators.BORDER_EMAIL)
    
    assert  'rgb(255, 105, 114)' in elements[0].value_of_css_property("border")
    assert  'rgb(255, 105, 114)' in elements[1].value_of_css_property("border")
    assert  'rgb(255, 105, 114)' in elements[2].value_of_css_property("border")
    
    assert 'Ошибка' in driver.find_element(*Locators.FIELD_WITH_ERROR_SIGN).text
    
    driver.quit() 
    

def test_registration_existing_user(driver, existing_user):

    WebDriverWait(driver, 10).until(
       EC.element_to_be_clickable(Locators.LOGIN_REG_BUTTON)
    ).click()
    
    driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()
    
    driver.find_element(*Locators.EMAIL_FIELD).send_keys(existing_user["email"])
    driver.find_element(*Locators.PASSWORD_FIELD).send_keys(existing_user["password"])
    driver.find_element(*Locators.CONFIRM_PASSWORD_FIELD).send_keys(existing_user["confirm_password"])

    driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 10).until(
         EC.presence_of_all_elements_located(Locators.BORDER_EMAIL)
    )
    elements = driver.find_elements(*Locators.BORDER_EMAIL)
    
    assert  'rgb(255, 105, 114)' in elements[0].value_of_css_property("border")
    assert  'rgb(255, 105, 114)' in elements[1].value_of_css_property("border")
    assert  'rgb(255, 105, 114)' in elements[2].value_of_css_property("border")
    
    assert 'Ошибка' in driver.find_element(*Locators.FIELD_WITH_ERROR_SIGN).text   
    
    driver.quit() 

