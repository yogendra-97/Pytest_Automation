import time

from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service
#-- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
#['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']

def test_url(browser):
    driver = browser
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
    time.sleep(4)

def test_result(browser):
    driver = browser
    results = driver.find_elements(By.XPATH, "//div[@class='products']/div")#list[]
    count = len(results)
    assert count > 0
    for result in results:
        result.find_element(By.XPATH, "div/button").click()

def test_checkout(browser):
    driver=browser
    driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()  #15
    driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

#total amount validation
def test_total(browser):
    driver = browser
    prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
    total = 0
    for price in prices:
        total = total + int(price.text)
    print(total)

    totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

    assert total == totalAmount

def test_remaining(browser):
    driver = browser
    driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
    driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
    wait = WebDriverWait(driver,5)
    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
    print(driver.find_element(By.CLASS_NAME,"promoInfo").text)



















