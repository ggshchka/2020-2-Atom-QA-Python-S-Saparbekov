import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from ui.locators.basic_locators import DashboardPageLocators, CreateCampaignPageLocators
from ui.pages.main_page import MainPage


class DashboardPage(MainPage):

    URL = 'https://target.my.com/dashboard'
    locators = DashboardPageLocators()

    def go_to_create_campaign_page(self):
        self.go_to_dashboard_page()
        try:
            self.click(self.locators.CREATE_ANOTHER_CAMPAIGN, 3)
        except TimeoutException:
            self.click(self.locators.CREATE_CAMPAIGN)

    def delete_campaign(self):
        self.click(self.locators.FIRST_CAMPAIGN_CHECKBOX)
        self.click(self.locators.GO_TABLE_CONTROL_BUTTON)
        self.click(self.locators.GO_DELETE_BUTTON)


class CreateCampaignPage(MainPage):

    URL = 'https://target.my.com/campaign/new'
    locators = CreateCampaignPageLocators()

    def create_campaign_traffic(
            self, campaign_link,
            campaign_name,
            img_path,
            legal_info
    ):
        self.wait().until(
            EC.visibility_of_element_located(
                self.locators.GO_TRAFFIC_BUTTON
            )
        )
        self.click(self.locators.GO_TRAFFIC_BUTTON)

        self.wait().until(
            EC.visibility_of_element_located(
                self.locators.CAMPAIGN_LINK_INPUT_BOX
            )
        )
        campaign_link_input_field = self.find(
            self.locators.CAMPAIGN_LINK_INPUT_BOX
        )
        campaign_link_input_field.clear()
        campaign_link_input_field.send_keys(campaign_link)

        self.wait(12).until(
            EC.visibility_of_element_located(
                self.locators.CAMPAIGN_NAME_INPUT_BOX
            )
        )
        campaign_name_input_field = self.find(
            self.locators.CAMPAIGN_NAME_INPUT_BOX
        )
        campaign_name_input_field.clear()
        campaign_name_input_field.send_keys(campaign_name)

        self.click(self.locators.GO_BANNER_FORMAT)

        campaign_img_input_field = self.find(
            self.locators.UPLOAD_IMG_INPUT
        )
        campaign_img_input_field.send_keys(img_path)

        campaign_legal_information_textarea = self.find(
            self.locators.LEGAL_INFORMATION_TEXTAREA
        )
        campaign_legal_information_textarea.clear()
        campaign_legal_information_textarea.send_keys(legal_info)

        self.move_to_element(self.locators.SLIDER_ICON)
        self.wait(5).until(
            EC.visibility_of_element_located(self.locators.GRAPH)
        )
        time.sleep(2)  # Внутренняя ошибка. Повторите попытку позже. Код ошибки: ...
        self.click(self.locators.CREATE_CAMPAIGN_BUTTON)
