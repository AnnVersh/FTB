# pages/login_page.py

from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://192.168.40.100:8000/login"

        # Locators
        self.username_field = (By.ID, "txtUsername")
        self.password_field = (By.ID, "txtPassword")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.error_message = (By.CSS_SELECTOR, ".alert.alert-dismissible.alert-danger")

    def load(self):
        """Load the login page."""
        self.driver.get(self.url)

    def login(self, username, password):
        """Perform the login action."""
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        """Get the error message text."""
        message = self.driver.find_element(*self.error_message).text.strip()
        return message.replace("×", "").strip()