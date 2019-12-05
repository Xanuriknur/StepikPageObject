from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK  = (By.LINK_TEXT, "View basket")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_SUMMARY = (By.CLASS_NAME, "basket_summary")
    TEXT_EMPTY_BASKET = (By.XPATH, '//p[contains(text(),"Your basket is empty.")]')

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    

class LoginPageLocators():
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    LOGIN_CONFRIM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_LOG_IN = (By.XPATH, '//button[@name="registration_submit"]')

class ProductPageLocators():
    BUTTON_ADD = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.XPATH, '//p[@class="price_color"]')
    PRODUCT_PRICE_IN_BASKET = (By.XPATH, '//strong[contains(text(), "Всего в корзине")]')
    ALERTINNER = (By.XPATH, '//div[contains(@class,"alertinner")]/strong[contains(text(), "The shellcoder\'s handbook")]')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages>div:nth-child(1)')