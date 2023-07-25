import  pytest
from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utility.locators import LoginLocators
from utility.locators import LogoutLocators
from utility.locators import MyAccountLocators
from utility.locators import RegisterLocators
from selenium.webdriver.support.select import Select
from utility.reusbale import ReUsableCode

class LoginPageController(ReUsableCode):
    def __init__(self,driver):
        self.driver =driver

    def login_user(self):
        log = self.getlogger()
        new_email = self.RegisterUser()
        self.driver.find_element(*LoginLocators.LOGIN_LINK).click()
        self.driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(new_email)
        self.driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(self.login_password)
        self.driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
        logout_link  = self.driver.find_element(*LogoutLocators.LOGOUT_LINK)
        log.info("Assertion to check enability of logout link")
        assert logout_link.is_enabled()
        logout_link.click()

    def login_unregisterd_user(self):
        log = self.getlogger()
        self.driver.find_element(*LoginLocators.LOGIN_LINK).click()
        self.driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(self.login_unregister_email)
        self.driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(self.login_unregister_password)
        self.driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
        LOGIN_FAILED_MESSAGE = self.driver.find_element(*LoginLocators.LOGIN_FAIL).text
        log.info("Assertion to un registered user cannot login")
        assert   LOGIN_FAILED_MESSAGE == self.login_fail_message











