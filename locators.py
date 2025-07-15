from selenium.webdriver.common.by import By


class Locators:
    LOGIN_REG_BUTTON = (By.XPATH, ".//button[text()='Вход и регистрация']")
    NO_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Нет аккаунта']")
    EMAIL_FIELD = (By.XPATH, ".//input[@placeholder='Введите Email']")
    PASSWORD_FIELD = (By.XPATH, ".//input[@placeholder='Пароль']")
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "input[placeholder='Повторите пароль']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Создать аккаунт']")
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выйти']")
    USER_NAME = (By.XPATH, ".//h3[@class='profileText name']")
    HOME_PAGE = (By.XPATH, "//*[contains(@class, 'homePage_homepage')]")
    AVATAR = (By.XPATH, ".//button[@class='circleSmall']")  
    BORDER_EMAIL = (By.CSS_SELECTOR, "form div.input_inputError__fLUP9")
    FIELD_WITH_ERROR_SIGN = (By.XPATH, ".//div/div/form[@class='popUp_shell__LuyqR']/div/div")
    CREATE_ADVERTISEMENT = (By.XPATH, ".//button[text()='Разместить объявление']")
    MODAL_WINDOW = (By.XPATH, ".//form[@class='popUp_shell__LuyqR']")
    MODAL_WINDOW_TEXT = (By.XPATH, ".//h1[text()='Чтобы разместить объявление, авторизуйтесь']")
    NAME_AD_FIELD = (By.CSS_SELECTOR, "input[placeholder='Название']")
    DESCRIPTION_AD_FIELD = (By.CSS_SELECTOR, "textarea[placeholder='Описание товара']")
    COST_AD_FIELD = (By.CSS_SELECTOR, "input[placeholder='Стоимость']")
    CATEGORY_DROP_DOWN = (By.XPATH, "//input[@name='category']/following-sibling::button[contains(@class, 'dropDownMenu_arrowDown__pfGL1')]")  
    CATEGORY_OPTIONS = (By.XPATH, "//div[@class='dropDownMenu_options__CmHmm']/button/span[text()='Книги']")
    CITY_DROP_DOWN = (By.XPATH, "//input[@name='city']/following-sibling::button[contains(@class, 'dropDownMenu_arrowDown__pfGL1')]") 
    CITY_OPTIONS = (By.XPATH, "//div[@class='dropDownMenu_options__CmHmm']/button/span[text()='Нижний Новгород']")
    RADIO_BUTTON_CONDITION = (By.CSS_SELECTOR, ".radioUnput_inputRegular__FbVbr")
    PUBLISH_BUTTON = (By.XPATH, ".//button[text()='Опубликовать']")
    MY_ADVERTISEMENTS = (By.XPATH, ".//div[@class='grid_threeColumns__ldn5D']") 
    CARDS_NAME = (By.CSS_SELECTOR, ".about h2")
    
    