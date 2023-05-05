from Pages.BasePage import Base_Page


class LoginPage(Base_Page):

    def __init__(self,driver):
        super().__init__(driver)


    def test_login(self,username,password):

        self.type('username_NAME',username)
        self.type('password_NAME',password)
        self.click('submit_ID')

