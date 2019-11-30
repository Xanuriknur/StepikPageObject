from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUTTON_ADD = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.XPATH, '//p[@class="price_color"]')
    PRODUCT_PRICE_IN_BASKET = (By.XPATH, '//strong[contains(text(), "Всего в корзине")]')
    ALERTINNER = (By.XPATH, '//div[contains(@class,"alertinner")]/strong[contains(text(), "The shellcoder\'s handbook")]')
    