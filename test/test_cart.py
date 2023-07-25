import  pytest
from page.cart_page import CartPageController

@pytest.mark.usefixtures("setup" , "log_on_failure")
class TestCart():


    def test_addtocart(self):
        CartPageControllerobject = CartPageController(self.driver)
        CartPageControllerobject.add_to_cart()

    def test_removefromcart(self):
        CartPageControllerobject = CartPageController(self.driver)
        CartPageControllerobject.remove_from_cart()



