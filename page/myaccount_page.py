import time
import  pytest
from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utility.locators import MyAccountLocators
from utility.locators import LoginLocators
from utility.locators import RegisterLocators
from  selenium.webdriver.support.select import Select
from utility.reusbale import ReUsableCode

class MyAccountPageController(ReUsableCode):
    def __init__(self,driver):
        self.driver =driver

    def verfiy_user_account(self):
        log = self.getlogger()
        new_email = self.RegisterUser()
        self.driver.find_element(*LoginLocators.LOGIN_LINK).click()
        self.driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(new_email)
        self.driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(self.register_password)
        self.driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
        self.driver.find_element(*MyAccountLocators.MYACCOUNT_LINK).click()
        first_name = self.driver.find_element(*RegisterLocators.FIRST_NAME_INPUT).get_attribute("value")
        log.info("Assertion to check user first name should be correct")
        assert first_name == self.register_first_name
        last_name = self.driver.find_element(*RegisterLocators.LAST_NAME_INPUT).get_attribute("value")
        log.info("Assertion to check user last name should be correct")
        assert last_name == self.register_last_name
        user_email = self.driver.find_element(*RegisterLocators.EMAIL_INPUT).get_attribute("value")
        log.info("Assertion to check user email should be correct")
        assert user_email == new_email
        customer_info_link = self.driver.find_element(*MyAccountLocators.CUSTOMER_INFO)
        log.info("Assertion to check enability of customer information link")
        assert customer_info_link.is_enabled()
        adddres_link = self.driver.find_element(*MyAccountLocators.CUSTOMER_ADDRESS)
        log.info("Assertion to check enability of customer address link")
        assert adddres_link.is_enabled()
        order_link = self.driver.find_element(*MyAccountLocators.CUSTOMER_ORDERS)
        log.info("Assertion to check enability of customer orders link")
        assert order_link.is_enabled()
        change_password_link = self.driver.find_element(*MyAccountLocators.CHANGE_PASSWORD)
        log.info("Assertion to check enability of change password button")
        assert change_password_link.is_enabled()
        back_in_stock_subscriptions_link = self.driver.find_element(*MyAccountLocators.BACK_IN_STOCK_SUBSCRIPTIONS)
        log.info("Assertion to check enability of backinstocksubscriptions link")
        assert back_in_stock_subscriptions_link.is_enabled()
        downloadable_products_link = self.driver.find_element(*MyAccountLocators.DOWNLOADABLE_PRODUCT)
        log.info("Assertion to check enability of downloadable product link")
        assert downloadable_products_link.is_enabled()
        product_reviews_link = self.driver.find_element(*MyAccountLocators.PRODUCT_REVIEWS)
        log.info("Assertion to check enability of product review link")
        assert product_reviews_link.is_enabled()
        reward_point_link = self.driver.find_element(*MyAccountLocators.REWARD_POINTS)
        log.info("Assertion to check enability of reward point link")
        assert reward_point_link.is_enabled()








