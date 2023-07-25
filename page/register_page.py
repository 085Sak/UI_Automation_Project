import  pytest
from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utility.locators import RegisterLocators
from  selenium.webdriver.support.select import Select
from utility.reusbale import ReUsableCode


class RegisterPageController(ReUsableCode):
    def __init__(self,driver):
        self.driver =driver

    @pytest.mark.order1
    def RegisterNewUser(self):
        log = self.getlogger()
        self.driver.find_element(*RegisterLocators.REGISTER_LINK).click()
        self.driver.find_element(*RegisterLocators.MALE_RADIO_BUTTON).click()
        self.driver.find_element(*RegisterLocators.FIRST_NAME_INPUT).send_keys(self.register_first_name)
        self.driver.find_element(*RegisterLocators.LAST_NAME_INPUT).send_keys(self.register_last_name)
        birth_date = Select(self.driver.find_element(*RegisterLocators.BIRTH_DAY))
        birth_date.select_by_value(self.register_birth_date)
        birth_month = Select(self.driver.find_element(*RegisterLocators.BIRTH_MONTH))
        birth_month.select_by_value(self.register_birth_month)
        birth_year = Select(self.driver.find_element(*RegisterLocators.BIRTH_YEAR))
        birth_year.select_by_value(self.register_birth_year)
        register_email= ReUsableCode.email_generator()
        self.driver.find_element(*RegisterLocators.EMAIL_INPUT).send_keys(register_email)
        self.driver.find_element(*RegisterLocators.COMPANY_NAME).send_keys(self.register_company_name)
        self.driver.find_element(*RegisterLocators.PASSWORD).send_keys(self.register_password)
        self.driver.find_element(*RegisterLocators.CONFIRM_PASSWORD).send_keys(self.register_password)
        self.driver.find_element(*RegisterLocators.SUBMIT_BUTTON).click()
        registration_complete_message = self.driver.find_element(*RegisterLocators.REGISTRATION_SUCCESSFUL_MESSAGE).text
        log.info("Assertion to check user regsitered Successfully")
        assert registration_complete_message == self.registration_success_message

    def RegisterWithIncompleteDetails(self):
        log = self.getlogger()
        self.driver.find_element(*RegisterLocators.REGISTER_LINK).click()
        self.driver.find_element(*RegisterLocators.MALE_RADIO_BUTTON).click()
        self.driver.find_element(*RegisterLocators.LAST_NAME_INPUT).send_keys(self.register_last_name)
        birth_date = Select(self.driver.find_element(*RegisterLocators.BIRTH_DAY))
        birth_date.select_by_value(self.register_birth_date)
        birth_month = Select(self.driver.find_element(*RegisterLocators.BIRTH_MONTH))
        birth_month.select_by_value(self.register_birth_month)
        birth_year = Select(self.driver.find_element(*RegisterLocators.BIRTH_YEAR))
        birth_year.select_by_value(self.register_birth_year)
        self.driver.find_element(*RegisterLocators.EMAIL_INPUT).send_keys(self.register_email)
        self.driver.find_element(*RegisterLocators.COMPANY_NAME).send_keys(self.register_company_name)
        self.driver.find_element(*RegisterLocators.PASSWORD).send_keys(self.register_password)
        self.driver.find_element(*RegisterLocators.CONFIRM_PASSWORD).send_keys(self.register_password)
        self.driver.find_element(*RegisterLocators.SUBMIT_BUTTON).click()
        FIRST_NAME_INCOMPLETE_MESSAGE = self.driver.find_element(*RegisterLocators.FIRST_NAME_ERROR).text
        log.info("Assertion to check user cannot register with incomplete detail")
        assert FIRST_NAME_INCOMPLETE_MESSAGE == self.register_first_name_incomplete_message


    def RegisterWithInvalidEmail(self):
        log = self.getlogger()
        self.driver.find_element(*RegisterLocators.REGISTER_LINK).click()
        self.driver.find_element(*RegisterLocators.MALE_RADIO_BUTTON).click()
        self.driver.find_element(*RegisterLocators.FIRST_NAME_INPUT).send_keys(self.register_first_name)
        self.driver.find_element(*RegisterLocators.LAST_NAME_INPUT).send_keys(self.register_last_name)
        birth_date = Select(self.driver.find_element(*RegisterLocators.BIRTH_DAY))
        birth_date.select_by_value(self.register_birth_date)
        birth_month = Select(self.driver.find_element(*RegisterLocators.BIRTH_MONTH))
        birth_month.select_by_value(self.register_birth_month)
        birth_year = Select(self.driver.find_element(*RegisterLocators.BIRTH_YEAR))
        birth_year.select_by_value(self.register_birth_year)
        self.driver.find_element(*RegisterLocators.EMAIL_INPUT).send_keys(self.register_invalid_email)
        self.driver.find_element(*RegisterLocators.COMPANY_NAME).send_keys(self.register_company_name)
        self.driver.find_element(*RegisterLocators.PASSWORD).send_keys(self.register_password)
        self.driver.find_element(*RegisterLocators.CONFIRM_PASSWORD).send_keys(self.register_password)
        self.driver.find_element(*RegisterLocators.SUBMIT_BUTTON).click()
        EMAIL_ERROR_MESSAGE = self.driver.find_element(*RegisterLocators.EMAIL_ERROR).text
        log.info("Assertion to check user cannot regsitered with invalid")
        assert EMAIL_ERROR_MESSAGE == self.register_email_error_message























