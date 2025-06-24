from selenium.webdriver.common.by import By

class RegisterPageLocators:
    USERNAME_FIELD = (By.ID, "sign-username")
    PASSWORD_FIELD = (By.ID, "sign-password")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Sign up') and contains(@onclick, 'register()')]")