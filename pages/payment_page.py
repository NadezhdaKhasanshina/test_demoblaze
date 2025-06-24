import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from locators.common_locators import CommonLocators
from locators.payment_locators import PaymentPageLocators


class PaymentPage(BasePage):
    def navigate_to_cart(self):
        self.wait_for_element(CommonLocators.CART_ICON).click()
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, "page-wrapper")))

    @allure.step("Заполнить платежные данные")
    def fill_payment_info(self, name, country, city, card, month, year):
        self.wait_for_element(PaymentPageLocators.NAME_FIELD).send_keys(name)
        self.wait_for_element(PaymentPageLocators.COUNTRY_FIELD).send_keys(country)
        self.wait_for_element(PaymentPageLocators.CITY_FIELD).send_keys(city)
        self.wait_for_element(PaymentPageLocators.CARD_NUMBER_FIELD).send_keys(card)
        self.wait_for_element(PaymentPageLocators.MONTH_FIELD).send_keys(month)
        self.wait_for_element(PaymentPageLocators.YEAR_FIELD).send_keys(year)

    @allure.step("Завершить покупку")
    def complete_purchase(self):
        self.wait_for_element(PaymentPageLocators.PURCHASE_BUTTON).click()