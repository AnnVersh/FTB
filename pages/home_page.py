# pages/home_page.py

from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        # Locator for the "Log out" button or other element that verifies successful login
        self.logout_button = (By.ID, "btnLogout")

    def is_logout_button_visible(self):
        """Check if the logout button is visible."""
        try:
            return self.driver.find_element(*self.logout_button).is_displayed()
        except:
            return False
