from selenium.webdriver.common.by import By

from Utilities.Configreader import readConfig
import logging
from Utilities.LogUtil import Logger

log = Logger(__name__,logging.INFO)
class Base_Page:

    def __init__(self,driver):
       self.driver=driver

    def type(self, locator, value):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH,readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_NAME"):
            self.driver.find_element(By.NAME,readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID,readConfig("locators", locator)).send_keys(value)
        log.logger.info("Typing in an element: " + str(locator) + " value entered as : " + str(value))


    def click(self, locator):

        if str(locator).endswith("_ID"):
            self.driver.find_element(By.ID,readConfig("locators", locator)).click()
        log.logger.info("Clicking on an element: " + str(locator))