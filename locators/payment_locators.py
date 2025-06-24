from selenium.webdriver.common.by import By

class PaymentPageLocators:
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[@data-target='#orderModal']")
    NAME_FIELD = (By.ID, "name")
    COUNTRY_FIELD = (By.ID, "country")
    CITY_FIELD = (By.ID, "city")
    CARD_NUMBER_FIELD = (By.ID, "card")
    MONTH_FIELD = (By.ID, "month")
    YEAR_FIELD = (By.ID, "year")
    PURCHASE_BUTTON = (By.XPATH, "//button[contains(text(),'Purchase') and @onclick='purchaseOrder()']")
    ORDER_MODAL = (By.ID, "orderModal")
    SUCCESS_PURCHASE_ALERT = (By.XPATH, "//div[contains(@class, 'sweet-alert')]")
    CONFIRM_BUTTON = (By.XPATH, "//button[contains(@class, 'confirm')]")