import pytest
import allure
import  random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from allure_commons.types import AttachmentType

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action ="store" , default = "chrome",
    )

@pytest.fixture(scope="class")
def setup(request):
    global  driver
    browser_name = request.config.getoption("browser_name")
    if (browser_name == "chrome"):
        # for headless mode
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # driver = webdriver.chrome(options= chrome_options)
        service_obj = Service("chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    else:
        service_obj = Service("geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://demo.nopcommerce.com/")
    request.cls.driver = driver
    yield
    driver.close()

@pytest.hookimpl(hookwrapper=True,tryfirst=True)
def pytest_runtest_makereport(item , call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item , "rep_" + rep.when, rep)

@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(),name="test failure", attachment_type= AttachmentType.PNG)
