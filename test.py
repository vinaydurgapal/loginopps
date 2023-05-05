import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(type(self).__name__)

    def wait_for_element(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            self.logger.info(f"Found element with locator '{locator}'.")
            return element
        except Exception as e:
            self.logger.error(f"Failed to find element with locator '{locator}'. Error: {e}")
            raise e


class LoginPage(BasePage):
    def __init__(self, driver):

        super().__init__(driver)
        self.driver=webdriver.Chrome()
        self.driver.get("https://practicetestautomation.com/practice-test-login/")
        self.username_field = (By.ID, "username")
        self.password_field = (By.ID, "password")
        self.login_button = (By.XPATH, "submit")

    def enter_username(self, username):
        self.wait_for_element(self.username_field).send_keys(username)
        self.logger.info(f"Entered username: {username}")

    def enter_password(self, password):
        self.wait_for_element(self.password_field).send_keys(password)
        self.logger.info(f"Entered password: {password}")

    def click_login_button(self):
        self.wait_for_element(self.login_button).click()
        self.logger.info("Clicked on login button.")
