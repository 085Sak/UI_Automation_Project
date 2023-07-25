import  pytest
from page.home_page import HomePageController

@pytest.mark.usefixtures("setup" , "log_on_failure")
class TestHome():

    def test_currency_changer(self):
        homepagecontrollerobject = HomePageController(self.driver)
        homepagecontrollerobject.verify_currency_changer()

    def test_search(self):
        homepagecontrollerobject = HomePageController(self.driver)
        homepagecontrollerobject.verify_search()

    def test_category(self):
        homepagecontrollerobject = HomePageController(self.driver)
        homepagecontrollerobject.verify_category_enabled()

    def test_product_feature_enabled(self):
        homepagecontrollerobject = HomePageController(self.driver)
        homepagecontrollerobject.verify_product_feature_enabled()

    def test_news_feature(self):
        homepagecontrollerobject = HomePageController(self.driver)
        homepagecontrollerobject.verify_news_features()

    def test_community_poll_feature(self):
        homepagecontrollerobject = HomePageController(self.driver)
        homepagecontrollerobject.verify_community_poll_feature()

    def test_social_media_link_enabled(self):
        homepagecontrollerobject = HomePageController(self.driver)
        homepagecontrollerobject.verify_social_media_link_enabled()

    def test_news_letter(self):
        homepagecontrollerobject = HomePageController(self.driver)
        homepagecontrollerobject.verify_news_letter()




