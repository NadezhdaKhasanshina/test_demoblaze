from selenium.webdriver.common.by import By

class LoginPageLocators:
    USERNAME_FIELD = (By.ID, "loginusername")
    PASSWORD_FIELD = (By.ID, "loginpassword")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Log in') and contains(@onclick, 'logIn()')]")