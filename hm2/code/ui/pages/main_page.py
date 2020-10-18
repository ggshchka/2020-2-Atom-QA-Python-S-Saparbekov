from ui.locators.basic_locators import MainPageLocators
from ui.pages.base_page import BasePage


class MainPage(BasePage):

    locators = MainPageLocators()

    def logout(self):
        self.click(self.locators.GO_PREV_LOGOUT_BUTTON)
        #time.sleep(0.5) # transition: transform 400ms
        self.move_to_element(self.locators.GO_LOGOUT_BUTTON)
        self.click(self.locators.GO_LOGOUT_BUTTON)

    def go_to_dashboard_page(self):
        self.click(self.locators.GO_CAMPAIGN_BUTTON)

    def go_to_segment_page(self):
        self.click(self.locators.GO_SEGMENT_BUTTON)