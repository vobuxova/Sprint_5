from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from Sprint_5.locators import Locators


def test_registration_existing_user(driver, existing_user):

    WebDriverWait(driver, 10).until(
       EC.element_to_be_clickable(Locators.LOGIN_REG_BUTTON)
    ).click()
    
    driver.find_element(*Locators.EMAIL_FIELD).send_keys(existing_user["email"])
    driver.find_element(*Locators.PASSWORD_FIELD).send_keys(existing_user["password"])
  

    driver.find_element(*Locators.LOGIN_BUTTON).click()
    
    assert 'https://qa-desk.stand.praktikum-services.ru/login' in driver.current_url

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.AVATAR))

    WebDriverWait(driver, 10).until(
       EC.element_to_be_clickable(Locators.LOGOUT_BUTTON)
    ).click()
    
    WebDriverWait(driver, 5).until(
            EC.invisibility_of_element_located(Locators.AVATAR)
    )
    
    WebDriverWait(driver, 5).until(
            EC.invisibility_of_element_located(Locators.USER_NAME)
    )
    
    assert driver.find_element(*Locators.LOGIN_REG_BUTTON)
    
    driver.quit() 