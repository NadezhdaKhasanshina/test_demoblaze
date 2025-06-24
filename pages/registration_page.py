from selenium.webdriver.support import expected_conditions as EC
import uuid
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from locators.register_locators import RegisterPageLocators

class RegistrationPage(BasePage):
    def fill_registration_form(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.submit_registration()

    def register_new_user(self, password="SecurePass123"):
        """Полный процесс регистрации с автоматической генерацией имени"""
        username = self.generate_username()
        self.fill_registration_form(username, password)
        return username

    def generate_username(self):
        """Генерирует уникальное имя пользователя"""
        return f"user_{uuid.uuid4().hex[:6]}"

    def fill_registration_form(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.submit_registration()

    def enter_username(self, username):
        field = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(RegisterPageLocators.USERNAME_FIELD)
        )
        field.click()
        field.send_keys(Keys.CONTROL + "a")
        field.send_keys(Keys.DELETE)
        field.send_keys(username)

    def enter_password(self, password):
        field = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(RegisterPageLocators.PASSWORD_FIELD)
        )
        field.click()
        field.send_keys(Keys.CONTROL + "a")
        field.send_keys(Keys.DELETE)
        field.send_keys(password)

    def submit_registration(self):
        button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(RegisterPageLocators.SUBMIT_BUTTON)
        )
        # Двойное действие для надёжности
        ActionChains(self.browser).move_to_element(button).click().perform()