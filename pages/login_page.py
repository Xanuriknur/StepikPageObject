from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    
    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        password_input.send_keys(password)
        confirm_password_input = self.browser.find_element(*LoginPageLocators.LOGIN_CONFRIM_PASSWORD)
        confirm_password_input.send_kyes(password)
        login_button = self.browser.find_element(*LoginPageLocators.BUTTON_LOG_IN)
        login_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес 
        assert self.browser.current_url == LoginPageLocators.LOGIN_URL, f"{self.browser.current_url} не равно {LoginPageLocators.LOGIN_URL}"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
