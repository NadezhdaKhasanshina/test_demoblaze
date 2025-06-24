from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.login_locators import LoginPageLocators

class LoginPage(BasePage):
    def fill_login_form(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def enter_username(self, username):
        field = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.USERNAME_FIELD)
        )
        field.click()
        field.send_keys(Keys.CONTROL + "a")
        field.send_keys(Keys.DELETE)
        field.send_keys(username)

    def enter_password(self, password):
        field = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.PASSWORD_FIELD)
        )
        field.click()
        field.send_keys(Keys.CONTROL + "a")
        field.send_keys(Keys.DELETE)
        field.send_keys(password)

    def click_login(self):
        button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.SUBMIT_BUTTON)
        )
        button.click()