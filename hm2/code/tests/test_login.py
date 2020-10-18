import pytest
from selenium.webdriver.remote.webelement import WebElement

from tests.base_case import BaseCase

@pytest.mark.UI
class TestLogin(BaseCase):

    @pytest.mark.usefixtures("login_logout")
    def test_login_url(self):
        assert self.driver.current_url == self.dashboard_page.URL


    @pytest.mark.parametrize(
        "email, password",
        [
            ('123456', 'crugerf001'),
            ('crugerf@mail.ru', 'crugerf000'),
        ]
    )
    def test_login_invalid_input(self, incorrect_login_go_source, email, password):
        element: WebElement = self.login_page.find(
            self.login_error_page.locators.INVALID_LOGIN_TEXTS
        )
        assert "https://account.my.com/login" in self.driver.current_url
        assert "Error" in element.text


    @pytest.mark.parametrize(
        "email, password",
        [
            ('123qwe', '00000'),
            ('_+321 0 )) ', '123qwe'),

        ]
    )
    def test_login_wrong_input(self, incorrect_login_go_source, email, password):
        self.login_page.find(self.login_page.locators.WRONG_LOGIN_TEXT)
        assert self.login_page.URL == self.driver.current_url
        assert "Введите email или телефон" in self.driver.page_source
