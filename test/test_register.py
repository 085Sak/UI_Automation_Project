import  pytest
from page.register_page import RegisterPageController

@pytest.mark.usefixtures("setup" , "log_on_failure")

class TestRegister():

    def test_register(self):
        registerpagecontrollerobject = RegisterPageController(self.driver)
        registerpagecontrollerobject.RegisterNewUser()

    def test_register_user_with_incomplete_details(self):
        registerpagecontrollerobject = RegisterPageController(self.driver)
        registerpagecontrollerobject.RegisterWithIncompleteDetails()

    def test_register_user_with_invalid_email(self):
        registerpagecontrollerobject = RegisterPageController(self.driver)
        registerpagecontrollerobject.RegisterWithInvalidEmail()

