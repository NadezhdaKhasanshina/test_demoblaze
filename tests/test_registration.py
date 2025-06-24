import pytest
from selenium.webdriver.common.by import By
import time
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Регистрация")
class TestRegistration:
    @allure.story("Успешная регистрация")
    def test_registration(self, browser):
        home_page = HomePage(browser)
        home_page.open_url()
        home_page.navigate_to_register()

        with allure.step("Создание новой учётной записи"):
            reg_page = RegistrationPage(browser)
            reg_page.register_new_user()
            time.sleep(1)

        with allure.step("Проверка успешного результата регистрации"):
            WebDriverWait(browser, 10).until(EC.alert_is_present())
            alert = browser.switch_to.alert
            assert "Sign up successful" in alert.text
            alert.accept()

    @allure.story("Ошибка повторной регистрации")
    def test_duplicate_username_error(self, browser):
        home_page = HomePage(browser)
        home_page.open_url()
        home_page.navigate_to_register()

        with allure.step("Попытка регистрации существующего пользователя"):
            reg_page = RegistrationPage(browser)
            reg_page.fill_registration_form("123new_user123", "securepass")

        with allure.step("Проверка наличия ошибки регистрации"):
            WebDriverWait(browser, 10).until(EC.alert_is_present())
            alert = browser.switch_to.alert
            assert "This user already exist." in alert.text
            alert.accept()
