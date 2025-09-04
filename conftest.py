import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()