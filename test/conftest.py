import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils.config import BASE_URL

@pytest.fixture(scope="session")
def browser():

    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    
    driver.quit()

@pytest.fixture(scope="function")
def base_url():
    return BASE_URL
