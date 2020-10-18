import random
import string

import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from ui.pages.base_page import BasePage
from ui.pages.dashboard_page import DashboardPage, CreateCampaignPage
from ui.pages.login_error_page import LoginErrorPage
from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage
from ui.pages.segment_page import SegmentPage, CreateSegmentPage


class UsupportedBrowserException(Exception):
    pass


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver=driver)


@pytest.fixture
def login_error_page(driver):
    return LoginErrorPage(driver=driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)


@pytest.fixture
def dashboard_page(driver):
    return DashboardPage(driver=driver)


@pytest.fixture
def create_campaign_page(driver):
    return CreateCampaignPage(driver=driver)


@pytest.fixture
def segment_page(driver):
    return SegmentPage(driver=driver)


@pytest.fixture
def create_segment_page(driver):
    return CreateSegmentPage(driver=driver)


@pytest.fixture(scope='function')
def driver(config):
    browser = config['browser']
    version = config['version']
    url = config['url']
    selenoid = config['selenoid']

    if browser == 'chrome':
        options = ChromeOptions()
        options.add_argument("--window-size=800,600")
        if selenoid:
            driver = webdriver.Remote(
                command_executor='http://127.0.0.1:4444/wd/hub/',
                options=options,
                desired_capabilities={
                    'acceptInsecureCerts': True,
                    'browserName': 'chrome',
                    'version': '',
                    'platform': 'ANY'
                }
            )
        else:
            manager = ChromeDriverManager(version=version)
            driver = webdriver.Chrome(
                executable_path=manager.install(),
                options=options,
                desired_capabilities={'acceptInsecureCerts': True}
            )

    elif browser == 'firefox':
        manager = GeckoDriverManager(version=version)
        driver = webdriver.Firefox(executable_path=manager.install())

    else:
        raise UsupportedBrowserException(f'Usupported browser: "{browser}"')

    driver.get(url)
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture(scope='function')
def login_logout(login_page, main_page):
    login_page.login('sff_ff@mail.ru', 'sff_ff001')
    yield main_page
    main_page.logout()


@pytest.fixture(scope='function')
def incorrect_login_go_source(login_page, driver, email, password):
    login_page.login(email, password)
    yield
    driver.get(login_page.URL)


@pytest.fixture(scope='function')
def generate_rand_campaign_param():
    yield {
        'camp_link': 'https://' + ''.join(random.choice(string.ascii_lowercase)
                                          for _ in range(random.randint(6, 10))) + '.test.com',
        'camp_name': 'THE ' + ''.join(random.choice(string.ascii_uppercase)
                                      for _ in range(random.randint(3, 6))),
        'legal_info': ''.join(random.choice(string.ascii_uppercase)
                              for _ in range(random.randint(6, 10)))
    }


@pytest.fixture(scope='function')
def create_delete_segment(segment_page, create_segment_page, segm_name="SEGMENT_NAME"):
    segment_page.go_to_create_segment_page()
    create_segment_page.create_segment(segm_name)
    yield
    segment_page.delete_segment()
