import  pytest
from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utility.locators import CartLocators
from utility.locators import WishListLocators
from utility.locators import LoginLocators
from utility.locators import LogoutLocators
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.support.select import Select
from utility.reusbale import ReUsableCode

class CartPageController(ReUsableCode):

    def __init__(self,driver):
        self.driver =driver

    def add_to_cart(self):
        log = self.getlogger()
        self.driver.find_element(*CartLocators.PRODUCT).click()
        self.driver.execute_script(self.cart_scroll_value)
        self.driver.find_element(*CartLocators.PRODUCT_ADD_TO_CART).click()
        product_name =self.driver.find_element(*CartLocators.PRODUCT_NAME).text
        product_qunatity =self.driver.find_element(*CartLocators.PRODUCT_QUANTITY).text
        product_price = self.driver.find_element(*CartLocators.PRODUCT_PRICE).text
        self.driver.find_element(*CartLocators.CART_PAGE).click()
        cart_page_title = self.driver.find_element(*CartLocators.CART_PAGE_TITLE).text
        log.info("Assertion to verify cart page tile")
        assert cart_page_title == self.cart_page_title
        added_product_name = self.driver.find_element(*CartLocators.CART_PAGE_PRODUCT_NAME).text
        added_product_price = self.driver.find_element(*CartLocators.CART_PAGE_PRODUCT_PRICE).text
        log.info("Assertion to check added product name")
        assert product_name == added_product_name
        log.info("Assertion to check added product price")
        assert product_price == added_product_price
        gift_wrap_field = self.driver.find_element(*CartLocators.GIFT_WRAP_SELECT_FIELD)
        log.info("Assertion to check gift wrap field is enabled")
        assert gift_wrap_field.is_enabled()
        discount_code_field = self.driver.find_element(*CartLocators.DISCOUNT_CODE_FIELD)
        log.info("Assertion to check discount field is enabled")
        assert discount_code_field.is_enabled()
        gift_card_field = self.driver.find_element(*CartLocators.GIFT_CARDS_FIELD)
        log.info("Assertion to check gift card field is enabled")
        assert gift_card_field.is_enabled()
        apply_coupon_button = self.driver.find_element(*CartLocators.APPLY_COUPON_BUTTON)
        log.info("Assertion to check apply coupon button is enabled")
        assert apply_coupon_button.is_enabled()
        add_gift_card_button = self.driver.find_element(*CartLocators.ADD_GIFT_CARD_BUTTON)
        log.info("Assertion to check add gift card button is enabled")
        assert  add_gift_card_button.is_enabled()

    def remove_from_cart(self):
        log = self.getlogger()
        self.driver.find_element(*CartLocators.REMOVE_PRODUCT_BUTTON).click()
        PRODUCT_REMOVE_MESSAGE = self.driver.find_element(*CartLocators.CART_EMPTY_MESSAGE).text
        log.info("Assertion to check product removed successfully")
        assert  PRODUCT_REMOVE_MESSAGE == self.remove_from_cart_message





















