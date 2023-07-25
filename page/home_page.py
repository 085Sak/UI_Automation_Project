import  pytest
from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.support.select import Select
from utility.locators import HomePageLocators
from utility.reusbale import ReUsableCode

class HomePageController(ReUsableCode):
    def __init__(self,driver):
        self.driver =driver

    def verify_currency_changer(self):
        log = self.getlogger()
        self.driver.find_element(*HomePageLocators.CURRENCY_SELECTOR).click()
        curreny_type  = Select(self.driver.find_element(*HomePageLocators.CURRENCY_SELECTOR))
        curreny_type.select_by_value(self.home_currency_value)
        price= self.driver.find_element(*HomePageLocators.PRICE).text
        price_symbol = price[0]
        print(price_symbol)
        assert price_symbol == self.currency_symbol

    def verify_search(self):
        log = self.getlogger()
        self.driver.find_element(*HomePageLocators.CURRENCY_SELECTOR).click()
        self.driver.find_element(*HomePageLocators.SEARCH_BAR).send_keys(self.search_product)
        self.driver.find_element(*HomePageLocators.SEARCH_BUTTON).click()
        result_product = self.driver.find_element(*HomePageLocators.SEARCH_RESULT_PRODUCT).text
        log.info("Assertion to sercah feature")
        assert result_product == self.search_product
        self.driver.find_element(*HomePageLocators.RETURN_HOME).click()

    def verify_category_enabled(self):
        log = self.getlogger()
        COMPUTER_CATEGORY = self.driver.find_element(*HomePageLocators.COMPUTER_CATEGORY)
        log.info("Assertion to check computer category is enabled")
        assert COMPUTER_CATEGORY.is_enabled()
        ELECTRONICS_CATEGORY = self.driver.find_element(*HomePageLocators.ELECTRONICS_CATEGORY)
        log.info("Assertion to check electronics category is enabled")
        assert ELECTRONICS_CATEGORY.is_enabled()
        APPAREL_CATEGORY = self.driver.find_element(*HomePageLocators.APPAREL_CATEGORY)
        log.info("Assertion to  check apparel category is enabled")
        assert APPAREL_CATEGORY.is_enabled()
        DIGITAL_DOWNLOADS_CATEGORY = self.driver.find_element(*HomePageLocators.DIGITAL_DOWNLOADS_CATEGORY)
        log.info("Assertion to check digital download category is enabled")
        assert DIGITAL_DOWNLOADS_CATEGORY.is_enabled()
        BOOKS_CATEGORY = self.driver.find_element(*HomePageLocators.BOOKS_CATEGORY)
        log.info("Assertion to check book category is enabled")
        assert BOOKS_CATEGORY.is_enabled()
        JEWELRY_CATEGORY = self.driver.find_element(*HomePageLocators.JEWELRY_CATEGORY)
        log.info("Assertion to check jewelry category is enabled")
        assert JEWELRY_CATEGORY.is_enabled()
        GIFTCARD_CATEGORY= self.driver.find_element(*HomePageLocators.GIFTCARD_CATEGORY)
        log.info("Assertion to check giftcard category is enabled")
        assert GIFTCARD_CATEGORY.is_enabled()

    def verify_product_feature_enabled(self):
        log = self.getlogger()
        add_to_cart_home = self.driver.find_element(*HomePageLocators.ADD_TO_CART_HOME)
        log.info("Assertion to add to cart is enabled")
        assert add_to_cart_home.is_enabled()
        wishlist_home = self.driver.find_element(*HomePageLocators.WISHLIST_HOME)
        log.info("Assertion to wishlist is enabled")
        assert wishlist_home.is_enabled()
        compare_home = self.driver.find_element(*HomePageLocators.COMPARELIST_HOME)
        log.info("Assertion to check compare feature is enabled")
        assert compare_home.is_enabled()

    def verify_news_features(self):
        log = self.getlogger()
        DETAILS_BUTTON = self.driver.find_element(*HomePageLocators.NEWS_DETAIL)
        log.info("Assertion to check details button  is enabled")
        assert DETAILS_BUTTON.is_enabled()
        VIEW_NEWS_ARCHIVE_LINK = self.driver.find_element(*HomePageLocators.VIEW_NEWS_ARCHIVE)
        log.info("Assertion to check view news archive link is enabled")
        assert VIEW_NEWS_ARCHIVE_LINK.is_enabled()

    def verify_community_poll_feature(self):
        log = self.getlogger()
        RATING_RADIO_BUTTON = self.driver.find_element(*HomePageLocators.RATING_RADIO_BUTTON)
        log.info("Assertion to check rating radio button is enabled")
        assert RATING_RADIO_BUTTON.is_enabled()
        VOTE_BUTTON =  self.driver.find_element(*HomePageLocators.VOTE_BUTTON)
        log.info("Assertion to check vote button is enabled")
        assert VOTE_BUTTON.is_enabled()

    def verify_social_media_link_enabled(self):
        log = self.getlogger()
        FACEBOOK_PAGE_LINK = self.driver.find_element(*HomePageLocators.FACEBOOK_PAGE)
        log.info("Assertion to check facebook page  is link enabled")
        assert FACEBOOK_PAGE_LINK.is_enabled()
        TWITTER_PAGE_LINK = self.driver.find_element(*HomePageLocators.TWITTER_PAGE)
        log.info("Assertion to check twitter page  is link enabled")
        assert TWITTER_PAGE_LINK.is_enabled()
        YOUTUBE_PAGE_LINK =  self.driver.find_element(*HomePageLocators.YOUTUBE_PAGE)
        log.info("Assertion to check facebook page link  is enabled")
        assert YOUTUBE_PAGE_LINK.is_enabled()
        NEWS_PAGE_LINK = self.driver.find_element(*HomePageLocators.NEWS_PAGE)
        log.info("Assertion to check news page link  is enabled")
        assert NEWS_PAGE_LINK.is_enabled()

    def verify_news_letter(self):
        log = self.getlogger()
        NEWS_LETTER_EMAIL_FIELD = self.driver.find_element(*HomePageLocators.NEWS_LETTER_EMAIL)
        log.info("Assertion to check news letter email field is enabled")
        assert NEWS_LETTER_EMAIL_FIELD.is_enabled()
        NEWS_LETTER_SUBSCRIBE_BUTTON = self.driver.find_element(*HomePageLocators.NEWS_LETTER_SUBSCRIBE)
        log.info("Assertion to check news letter subscribe button is enabled")
        assert NEWS_LETTER_SUBSCRIBE_BUTTON.is_enabled()











