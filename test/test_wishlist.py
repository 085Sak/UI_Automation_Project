import  pytest
from page.wishlist_page import WishListPageController


@pytest.mark.usefixtures("setup" , "log_on_failure")
class TestWishlist():

    def test_add_to_wishlist(self):
        wishlistpagecontrollerobject = WishListPageController(self.driver)
        wishlistpagecontrollerobject.add_to_wishlist()

