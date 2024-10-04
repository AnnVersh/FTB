from selenium.webdriver.common.by import By

# tests/test_login.py

from pages.login_page import LoginPage
from pages.home_page import HomePage

def test_login_valid_credentials(driver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    
    login_page.load()
    login_page.login("john", "john123")
    
    assert home_page.is_logout_button_visible(), "Login was not successful!"

def test_login_with_capital_letter_username(driver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    
    login_page.load()
    login_page.login("John", "john123")
    
    assert home_page.is_logout_button_visible(), "Login was not successful with capital letter username!"

def test_login_with_empty_credentials(driver):
    login_page = LoginPage(driver)
    
    login_page.load()
    login_page.login("", "")
    
    error_message = login_page.get_error_message()
    assert error_message == "Invalid username and/or password.", "Error message text does not match"
    assert "?error" in driver.current_url, "User was not redirected to the error page"

def test_login_with_invalid_credentials(driver):
    login_page = LoginPage(driver)
    
    login_page.load()
    login_page.login("Mike", "john123")
    
    error_message = login_page.get_error_message()
    assert error_message == "Invalid username and/or password.", "Error message text does not match"
    assert "?error" in driver.current_url, "User was not redirected to the error page"
