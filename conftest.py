import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

#Precondition: browser is opened
@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()    # opens a fullscreen browser window
    driver.implicitly_wait(3)
    yield driver
    driver.quit()  #close the browser after test