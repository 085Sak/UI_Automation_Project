import  pytest
from page.login_page import LoginPageController

@pytest.mark.usefixtures("setup" , "log_on_failure")
class TestRegister():

    def test_login_registered_user(self):
        loginpagecontrollerobject = LoginPageController(self.driver)
        loginpagecontrollerobject.login_user()

    def test_login_unregistered_user(self):
        loginpagecontrollerobject = LoginPageController(self.driver)
        loginpagecontrollerobject.login_unregisterd_user()



