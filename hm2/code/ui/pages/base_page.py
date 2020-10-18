from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ui.locators import basic_locators

RETRY_COUNT = 300


class BasePage(object):

    locators = basic_locators.BasePageLocators()

    def __init__(self, driver):
        self.driver = driver

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 6
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator, timeout=None):
        for i in range(RETRY_COUNT):
            try:
                self.find(locator)
                element = self.wait(timeout).until(
                    EC.element_to_be_clickable(locator)
                )
                #self.scroll_to_element(element)
                element.click()
                return
            except StaleElementReferenceException:
                if i < RETRY_COUNT - 1:
                    pass
        raise

    def scroll_to_element(self, element):
        self.driver.execute_script(
            'arguments[0].scrollIntoView(true);',
            element
        )

    def move_to_element(self, locator):
        mv_to = self.find(locator)
        ActionChains(self.driver).move_to_element(mv_to).perform()
