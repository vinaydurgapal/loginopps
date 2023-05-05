
from TestCases.BaseTest import BaseTest
from Pages.LoginPage import  LoginPage
import logging
from Utilities.LogUtil import Logger

log = Logger(__name__,logging.INFO)
class Test_login:

    def test_doSignUp(self,get_browser):
        self.driver=get_browser
        log.logger.info("Test Do Sign up started")
        regPage = LoginPage(self.driver)
        print(" hello")
        regPage.test_login(
            username='username',password='passowrd'

        )


        log.logger.info("Test Do Sign up successfully executed")