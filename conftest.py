import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def browser():
    options = webdriver.ChromeOptions()             #в options складываем все настройки Chrome
    #options.add_argument("--headless")             #что бы тести были без визуалки
    browser = webdriver.Chrome(options=options)     #Указываем что будем использовать Chrome и его настройки options
    browser.maximize_window()                       #открыть браузер в полное окно
    yield browser                                   #остановка браузера
    browser.quit()

