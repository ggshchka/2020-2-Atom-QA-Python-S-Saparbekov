from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from ui.locators.basic_locators import CreateSegmentPageLocators, SegmentPageLocators
from ui.pages.main_page import MainPage


class SegmentPage(MainPage):

    URL = 'https://target.my.com/segments/segments_list'
    locators = SegmentPageLocators()

    def go_to_create_segment_page(self):
        self.go_to_segment_page()
        try:
            self.click(self.locators.CREATE_SEGMENT, 0.5)
        except TimeoutException:
            self.click(self.locators.CREATE_ANOTHER_SEGMENT)

    def delete_segment(self):
        self.click(self.locators.DELETE_NEW_SEGMENT)
        self.click(self.locators.CONFIRM_DELETE_BUTTON)
        self.wait().until(
            EC.invisibility_of_element_located(
                self.locators.CONFIRM_DELETE_BUTTON
            )
        )

    def count_of_segments(self):
        cnt = self.find(self.locators.COUNT_OF_SEGMENTS).text
        return int(cnt)


class CreateSegmentPage(MainPage):
    URL = 'https://target.my.com/segments/segments_list/new'
    locators = CreateSegmentPageLocators()

    def create_segment(self, name):
        self.click(self.locators.SEGMENT_CHECKBOX)
        self.click(self.locators.ADD_SEGMENT_BUTTON)

        segment_input_name_field = self.find(
            self.locators.SEGMENT_NAME_INPUT
        )
        segment_input_name_field.clear()
        segment_input_name_field.send_keys(name)

        self.click(self.locators.CREATE_SEGMENT_BUTTON)
