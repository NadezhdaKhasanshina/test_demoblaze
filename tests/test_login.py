import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.login_locators import LoginPageLocators
from pages.home_page import HomePage
from pages.login_page import LoginPage
import time

@allure.feature("Авторизация")
class TestLogin:
    @allure.story("Успешная авторизация")
    def test_valid_user_login(self, browser):
        home_page = HomePage(browser)
        home_page.open_url()
        home_page.navigate_to_login()

        with allure.step("Заполнение данных существующего пользователя"):
            login_page = LoginPage(browser)
            login_page.fill_login_form("123new_user123", "securepass")


        with allure.step("Проверка успешной авторизации"):
            WebDriverWait(browser, 10).until(
                EC.invisibility_of_element_located(LoginPageLocators.SUBMIT_BUTTON))
            welcome_text = WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located((By.ID, "nameofuser")))
            assert "Welcome 123new_user123" in welcome_text.text

    @allure.story("Неуспешная авторизация с неверными данными")
    def test_invalid_credentials(self, browser):
        home_page = HomePage(browser)
        home_page.open_url()
        home_page.navigate_to_login()

        with allure.step("Заполнение неверных данных пользователя"):
            login_page = LoginPage(browser)
        login_page.enter_username("123new_user123")
        login_page.enter_password("ss")
        login_page.click_login()

        with allure.step("Проверка сообщения об ошибке"):
            WebDriverWait(browser, 10).until(EC.alert_is_present())
            alert = browser.switch_to.alert
            assert "Wrong password." in alert.text or "User does not exist." in alert.text
            alert.accept()

