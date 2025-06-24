import allure
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.payment_locators import PaymentPageLocators
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.payment_page import PaymentPage

@allure.feature("Покупка товара")
class TestFullTransaction:
    def test_full_transaction(self, browser):
        payment_data = {
            "name": "Иван",
            "country": "Россия",
            "city": "Москва",
            "card": "123",
            "month": "06",
            "year": "2025"
        }

        with allure.step("Авторизация существующего пользователя"):
            home_page = HomePage(browser)
            home_page.open_url()
            home_page.navigate_to_login()

            login_page = LoginPage(browser)
            login_page.fill_login_form("123new_user123", "securepass")
            WebDriverWait(browser, 10).until(
                EC.text_to_be_present_in_element((By.ID, "nameofuser"), "Welcome"))

        with allure.step("Добавление товара в корзину"):
            product_page = ProductPage(browser)
            product_page.select_third_item()
            time.sleep(2)

            product_page.add_to_cart()

        with allure.step("Проверка сообщения о добавлении"):
            WebDriverWait(browser, 10).until(EC.alert_is_present())
            alert = browser.switch_to.alert
            assert "Product added." in alert.text
            alert.accept()

        with allure.step("Оформление заказа"):
            payment_page = PaymentPage(browser)
            payment_page.navigate_to_cart()

            WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable(PaymentPageLocators.PLACE_ORDER_BUTTON)).click()

            WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located(PaymentPageLocators.ORDER_MODAL))

            payment_page.fill_payment_info(**payment_data)

            payment_page.complete_purchase()

        with allure.step("Проверка успешного оформления"):
            WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located(PaymentPageLocators.SUCCESS_PURCHASE_ALERT))

            confirmation = browser.find_element(*PaymentPageLocators.SUCCESS_PURCHASE_ALERT).text
            assert "Thank you for your purchase!" in confirmation

            # Закрытие модального окна
            browser.find_element(*PaymentPageLocators.CONFIRM_BUTTON).click()



