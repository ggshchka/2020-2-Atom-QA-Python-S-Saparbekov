import time

from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class LoginPage(BasePage):

    URL = 'https://target.my.com/'
    locators = basic_locators.LoginPageLocators()

    def go_login_page_from_source(self):
        self.click(self.locators.GO_PREV_LOGIN_BUTTON)

    def login(self, email, password):
        self.go_login_page_from_source()

        email_input_field = self.find(self.locators.EMAIL_INPUT)
        email_input_field.clear()
        email_input_field.send_keys(email)

        password_input_field = self.find(self.locators.PASSWORD_INPUT)
        password_input_field.clear()
        password_input_field.send_keys(password)

        self.click(self.locators.GO_LOGIN_BUTTON)
