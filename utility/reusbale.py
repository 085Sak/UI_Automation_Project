import  pytest
import logging
import random
from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utility.locators import RegisterLocators
from  selenium.webdriver.support.select import Select
from utility.config import DataSet

class ReUsableCode(DataSet):

    def __init__(self,driver):
        self.driver =driver


    def getlogger(self):
        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def RegisterUser(self):
        new_email = ReUsableCode.email_generator()
        self.driver.find_element(*RegisterLocators.REGISTER_LINK).click()
        self.driver.find_element(*RegisterLocators.MALE_RADIO_BUTTON).click()
        self.driver.find_element(*RegisterLocators.FIRST_NAME_INPUT).send_keys("abc")
        self.driver.find_element(*RegisterLocators.LAST_NAME_INPUT).send_keys("abc")
        birth_date = Select(self.driver.find_element(*RegisterLocators.BIRTH_DAY))
        birth_date.select_by_value("19")
        birth_month = Select(self.driver.find_element(*RegisterLocators.BIRTH_MONTH))
        birth_month.select_by_value("8")
        birth_year = Select(self.driver.find_element(*RegisterLocators.BIRTH_YEAR))
        birth_year.select_by_value("2000")
        self.driver.find_element(*RegisterLocators.EMAIL_INPUT).send_keys(new_email)
        self.driver.find_element(*RegisterLocators.COMPANY_NAME).send_keys("abc")
        self.driver.find_element(*RegisterLocators.PASSWORD).send_keys("abc@123")
        self.driver.find_element(*RegisterLocators.CONFIRM_PASSWORD).send_keys("abc@123")
        self.driver.find_element(*RegisterLocators.SUBMIT_BUTTON).click()
        return new_email

    def email_generator():
        validchars = 'abcdefghijklmnopqrstuvwxyz1234567890'
        loginlen = random.randint(4, 15)
        login = ''
        for i in range(loginlen):
            pos = random.randint(0, len(validchars) - 1)
            login = login + validchars[pos]
        if login[0].isnumeric():
            pos = random.randint(0, len(validchars) - 10)
            login = validchars[pos] + login
        servers = ['@gmail', '@yahoo', '@redmail', '@hotmail', '@bing']
        servpos = random.randint(0, len(servers) - 1)
        email = login + servers[servpos]
        tlds = ['.com', '.in', '.gov', '.ac.in', '.net', '.org']
        tldpos = random.randint(0, len(tlds) - 1)
        email = email + tlds[tldpos]
        return email


