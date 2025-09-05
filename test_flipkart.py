
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

# uservar= webdriver.ChromeOptions()
# uservar.add_argument("headless")
# uservar.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome()
#driver = webdriver.Chrome(options=uservar)
driver.implicitly_wait(3)
driver.maximize_window()

def test_flipkart():

    driver.get("https://www.flipkart.com")

    # # Opening new tab in Browser
    # driver.execute_script("window.open('');")
    # time.sleep(1)
    # driver.execute_script("window.open('');")
    # dr= driver.window_handles
    # time.sleep(1)
    # driver.switch_to.window(dr[0])
    # time.sleep(1)
    # driver.close()

    demo = driver.find_element(By.NAME, "q").get_attribute("placeholder")
    print(demo)
    demo = driver.find_element(By.NAME, "q")
    demo.send_keys("5G Smartphone under 20000")
    demo.send_keys(Keys.ENTER)
    #demo.send_keys(Keys.RETURN)

    try:
        # // waiting for specific web element before we move to the next script.
        offer = WebDriverWait(driver, 10)
        offer.until(EC.presence_of_element_located((By.XPATH, "//html/body/div[1]/div/div[2]/div/div/a[2]")))
        print("\nJust checking exception Handling for " + offer.text)

    except:
        print("No offer are available for you, checkout later..!!")

def test_cont():
    try:
        samsung = driver.find_element(By.XPATH, "//html/body/div[1]/div/div[3]/div[1]/div[1]/div/div[1]/div/section[3]/div[2]/div[1]/div[1]/input")
        print(samsung.get_attribute("title"))
        samsung.send_keys("Samsung")
        scx = driver.find_element(By.XPATH, "//html/body/div[1]/div/div[3]/div[1]/div[1]/div/div[1]/div/section[3]/div[2]/div[1]/div[2]/div/label/div[1]").click()

        three = driver.find_element(By.XPATH, "//html/body/div[1]/div/div[3]/div/div[2]/div[26]/div/div/nav/a[3]").click()

        m34 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.LINK_TEXT, "SAMSUNG Galaxy M34 5G without charger (Prism Silver, 128 GB)"))
        )
        print("We found " + m34.text)

    except:
        pass
    #     print('We could not find "SAMSUNG Galaxy M34 5G without charger (Prism Silver, 128 GB)"')

def test_cont2():

    try:
        m15 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.LINK_TEXT, "SAMSUNG M15 (Blue Topaz, 128 GB)"))
        )
        m15.click()

        m15bn = driver.find_element(By.LINK_TEXT, "Buy Now")
        driver.close()

    except:
        pass
    #     print('We could not find "SAMSUNG M15 (Blue Topaz, 128 GB)"')


    fkh = driver.find_element(By.CLASS_NAME, "W5mR4e").click()

    try:
        driver.find_element(By.CLASS_NAME, "_30XB9F").click()
    except:
        pass
    #     print("Login Page closed")

def test_cont3():

    try:
        zb = WebDriverWait(driver, 12).until(
            EC.presence_of_element_located((By.XPATH, "_1krdK5 _3jeYYh"))
        )
        zb.click()

        zbbn = driver.find_element(By.CLASS_NAME, "OGrnIL")

        driver.close()

    except:
        pass
    #     print('We could not complete any of the requests, hence closing the browser..!!')

    driver.quit()