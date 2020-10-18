import pytest
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.support import expected_conditions as EC

from tests.base_case import BaseCase

@pytest.mark.UI
class TestCreateCampaignAndSegment(BaseCase):

    @pytest.mark.usefixtures("login_logout")
    def test_create_campaign(self, generate_rand_campaign_param):
        _link = generate_rand_campaign_param['camp_link']
        _name = generate_rand_campaign_param['camp_name']
        _legal_info = generate_rand_campaign_param['legal_info']
        self.dashboard_page.go_to_create_campaign_page()
        assert self.driver.current_url == self.create_campaign_page.URL
        self.create_campaign_page.create_campaign_traffic(
            campaign_link=_link,
            campaign_name=_name,
            img_path="hm2\\media\\img.png",
            legal_info=_legal_info
        )
        assert _name == self.dashboard_page.find(
            self.dashboard_page.locators.CAMPAIGN_NAME_CHECK
        ).text
        self.dashboard_page.delete_campaign()


    @pytest.mark.usefixtures("login_logout")
    def test_create_segment(self, create_delete_segment):
        assert self.create_segment_page.URL in self.driver.current_url
        segment_name = self.segment_page.find(
            self.segment_page.locators.NEW_SEGMENT_NAME_CHECK
        )
        assert segment_name.text == 'SEGMENT_NAME'


    @pytest.mark.usefixtures("login_logout")
    def test_delete_segment(self):
        name = "SEGMENT!!!"
        self.segment_page.go_to_create_segment_page()
        self.create_segment_page.create_segment(name)
        self.segment_page.wait().until(
            EC.visibility_of_all_elements_located(
                self.segment_page.locators.ALL_SEGMENTS
            )
        )
        cnt_on_table = len(
            self.driver.find_elements(
                *self.segment_page.locators.ALL_SEGMENTS
            )
        )
        if cnt_on_table > 1:
            next_segment_id = self.segment_page.find(
                self.segment_page.locators.NEXT_SEGMENT_ID_CHECK
            ).text
            self.segment_page.delete_segment()
            assert next_segment_id == self.segment_page.find(
                self.segment_page.locators.NEW_SEGMENT_ID_CHECK
            ).text
            with pytest.raises(TimeoutException):
                self.segment_page.wait(0.5).until(
                    EC.visibility_of_element_located(
                        self.segment_page.locators.INSTRUCTIONS
                    )
                )
        else:
            self.segment_page.delete_segment()
            self.segment_page.wait().until(
                EC.visibility_of_element_located(
                    self.segment_page.locators.CREATE_SEGMENT
                )
            )
            assert self.segment_page.count_of_segments() == 0
