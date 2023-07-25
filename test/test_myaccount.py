import  pytest
from page.myaccount_page import MyAccountPageController

@pytest.mark.usefixtures("setup" , "log_on_failure")
class TestMyAccount():

    def test_user_account(self):
        myaccountpagecontrollerobject = MyAccountPageController(self.driver)
        myaccountpagecontrollerobject.verfiy_user_account()
