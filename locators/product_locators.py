from selenium.webdriver.common.by import By

class ProductLocators:
    ITEM = (By.XPATH, "// h4 / a[contains( @ href, 'idp_=3')]")
    ADD_TO_CART_BTN = (By.XPATH, "//a[contains(text(),'Add to cart') and @onclick='addToCart(3)']")

