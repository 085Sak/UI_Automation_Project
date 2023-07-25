import  pytest
from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.support.select import Select
from utility.locators import WishListLocators
from utility.locators import CartLocators
from utility.reusbale import ReUsableCode

class WishListPageController(ReUsableCode):
    def __init__(self,driver):
        self.driver =driver

    def add_to_wishlist(self):
        log = self.getlogger()
        self.driver.find_element(*CartLocators.PRODUCT).click()
        self.driver.find_element(*WishListLocators.PRODUCT_ADD_TO_WISHLIST).click()
        product_name = self.driver.find_element(*CartLocators.PRODUCT_NAME).text
        product_qunatity = self.driver.find_element(*CartLocators.PRODUCT_QUANTITY).text
        product_price = self.driver.find_element(*CartLocators.PRODUCT_PRICE).text
        self.driver.find_element(*WishListLocators.WISHLIST_PAGE).click()
        wishlis_page_title =  self.driver.find_element(*WishListLocators.WISHLIST_PAGE_TITLE).text
        log.info("Assertion to check the title of wishlis page")
        assert wishlis_page_title == self.wishlist_page_title
        added_product_name = self.driver.find_element(*CartLocators.CART_PAGE_PRODUCT_NAME).text
        added_product_price = self.driver.find_element(*CartLocators.CART_PAGE_PRODUCT_PRICE).text
        log.info("Asserting added product name in wishlist")
        assert product_name == added_product_name
        log.info("Asserting added product price in wishlist")
        assert product_price == added_product_price
        update_wishlist_button = self.driver.find_element(*WishListLocators.UPDATE_WISHLIST)
        log.info("Assertion to check enablity of update wishlist button")
        assert  update_wishlist_button.is_enabled()
        email_friend_button = self.driver.find_element(*WishListLocators.EMAIL_FRIEND)
        log.info("Assertion to check enablity of email_friend button ")
        assert email_friend_button.is_enabled()
        add_to_cart_checkbox = self.driver.find_element(*WishListLocators.ADD_TO_CART_CHECKBOX)
        log.info("Assertion to check add to cart button enability")
        assert add_to_cart_checkbox.is_enabled()
        add_to_cart_wishlist_button = self.driver.find_element(*WishListLocators.ADD_TO_CART_WISHLISTBUTTON)
        log.info("Assertion to check add to wishlist button enability")
        assert add_to_cart_wishlist_button.is_enabled()
        






