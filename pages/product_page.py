from pages.base_page import BasePage
from locators.product_locators import ProductLocators
import allure

class ProductPage(BasePage):
    @allure.step("Выбрать третий товар из списка")
    def select_third_item(self):
        self.wait_for_element(ProductLocators.ITEM).click()

    @allure.step("Добавить товар в корзину")
    def add_to_cart(self):
        self.wait_for_element(ProductLocators.ADD_TO_CART_BTN).click()