import  pytest
from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utility.locators import LogoutLocators
from utility.locators import LoginLocators
from  selenium.webdriver.support.select import Select
from utility.reusbale import ReUsableCode


class LoginPageController(ReUsableCode):
    def __init__(self,driver):
        self.driver =driver

    def logout_user(self):
        log = self.getlogger()
        self.driver.find_element(*LoginLocators.LOGIN_LINK).click()
        log.info("Providing email")
        self.driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(self.login_email)
        log.info("Providing password")
        self.driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(self.login_password)
        self.driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
        self.driver.find_element(*LogoutLocators.LOGOUT_LINK).click()
        login_link = self.driver.find_element(*LoginLocators.LOGIN_LINK).click()
        log.info("Assertion to check enability of login link")
        assert login_link.is_enbaled()





