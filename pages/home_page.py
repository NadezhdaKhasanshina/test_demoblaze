from pages.base_page import BasePage
from locators.common_locators import CommonLocators
import allure

class HomePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("Открытие домашней страницы")
    def open_url(self):
        self.browser.get('https://www.demoblaze.com/')

    def navigate_to_login(self):
        self.wait_for_element(CommonLocators.LOGIN_BUTTON).click()

    def navigate_to_register(self):
        self.wait_for_element(CommonLocators.REGISTER_BUTTON).click()

    def add_item_to_cart(self, item_link):
        element = self.wait_for_element(item_link)
        element.click()
        self.wait_for_element(HomePageLocators.ADD_TO_CART_BUTTON).click()