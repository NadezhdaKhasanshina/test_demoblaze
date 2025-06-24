from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def wait_for_element(self, locator, timeout=10):
        """Ожидание появления элемента"""
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located(locator))

    def find(self, args):
        return self.browser.find_element(*args)