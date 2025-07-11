from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from Sprint_5.locators import Locators

def test_creating_ad_by_unauthorized_user(driver):

    WebDriverWait(driver, 10).until(
       EC.element_to_be_clickable(Locators.CREATE_ADVERTISEMENT)
    ).click()
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.MODAL_WINDOW))

    text = driver.find_element(*Locators.MODAL_WINDOW_TEXT).text
    assert text == 'Чтобы разместить объявление, авторизуйтесь'
    
    driver.quit() 
    
def test_creating_ad_by_authorized_user(driver, existing_user, create_ad):

    WebDriverWait(driver, 10).until(
       EC.element_to_be_clickable(Locators.LOGIN_REG_BUTTON)
    ).click()
    
    driver.find_element(*Locators.EMAIL_FIELD).send_keys(existing_user["email"])
    driver.find_element(*Locators.PASSWORD_FIELD).send_keys(existing_user["password"])
  
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(Locators.AVATAR))
   
    driver.find_element(*Locators.CREATE_ADVERTISEMENT).click()
    
    driver.find_element(*Locators.NAME_AD_FIELD).send_keys(create_ad["name"])
    driver.find_element(*Locators.DESCRIPTION_AD_FIELD).send_keys(create_ad["description"])
    driver.find_element(*Locators.COST_AD_FIELD).send_keys(create_ad["cost"])
    
    driver.find_element(*Locators.CATEGORY_DROP_DOWN).click()
    driver.find_element(*Locators.CATEGORY).click()
    
    driver.find_element(*Locators.CITY_DROP_DOWN).click()
    driver.find_element(*Locators.CITY).click()
    
    driver.find_element(*Locators.RABIO_BUTTON_CONDITION).click()
    driver.find_element(*Locators.PUBLISH_BUTTON).click()
    
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located(Locators.HOME_PAGE))
    driver.find_element(*Locators.AVATAR).click()
    
    WebDriverWait(driver, 10).until(
       EC.presence_of_element_located(Locators.MY_ADVERTISEMENTS)
    )
    
    element = driver.find_element(*Locators.MY_ADVERTISEMENTS)
    driver.execute_script("arguments[0].scrollIntoView();", element) 
    
    WebDriverWait(driver, 15).until(
       EC.presence_of_element_located(Locators.CARDS_NAME)
    )
    
    elements = driver.find_elements(*Locators.CARDS_NAME)
    assert elements[-1].text == create_ad["name"]

    driver.quit()