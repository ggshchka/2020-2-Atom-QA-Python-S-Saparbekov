import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage
from ui.pages.dashboard_page import DashboardPage, CreateCampaignPage
from ui.pages.login_error_page import LoginErrorPage
from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage
from ui.pages.segment_page import SegmentPage, CreateSegmentPage


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.login_page: LoginPage = request.getfixturevalue('login_page')
        self.login_error_page: LoginErrorPage = request.getfixturevalue(
            'login_error_page'
        )
        self.main_page: MainPage = request.getfixturevalue('main_page')
        self.dashboard_page: DashboardPage = request.getfixturevalue(
            'dashboard_page'
        )
        self.create_campaign_page: CreateCampaignPage = request.getfixturevalue(
            'create_campaign_page'
        )
        self.segment_page: SegmentPage = request.getfixturevalue(
            'segment_page'
        )
        self.create_segment_page: CreateSegmentPage = request.getfixturevalue(
            'create_segment_page'
        )
