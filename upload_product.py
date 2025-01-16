from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
import pytest
import time

@pytest.fixture
def setup_driver():
    # Set up the Selenium WebDriver with Microsoft Edge
    # webdriver_service = Service(r'D:\SETUPS\EdgeDriver_win64\edgedriver_win64\msedgedriver.exe')
    # driver = webdriver.Edge(service=webdriver_service)
    driver = webdriver.Edge()
    yield driver

def test_admin_upload_product(setup_driver):
    driver = setup_driver
    driver.get("http://localhost:5000/login")

    # Admin login
    #driver.find_element(By.NAME, "email").send_keys("njipditertullien19@gmail.com")
    #time.sleep(3)
    #driver.find_element(By.NAME, "password").send_keys("Tertu2005")
    #time.sleep(3)

    print('////////////////')
    driver.find_element(By.NAME, "email").send_keys("bongyu@gmail.com")
    time.sleep(3)
    driver.find_element(By.NAME, "password").send_keys("12345678")
    time.sleep(3)
    driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
    driver.find_element(By.NAME, "login").click()
    time.sleep(1)
    # driver.find_element(By.NAME, "code").send_keys("john1234")
    # time.sleep(3)
    # driver.find_element(By.NAME, "code").send_keys(Keys.RETURN)

    print('////////////////')
    # Navigate to product upload section
    driver.find_element(By.LINK_TEXT, "New Dish").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Add to Todays menu").click()
    time.sleep(3)

    # Fill out the product upload form
    driver.find_element(By.NAME, "name").send_keys("Fried Rice and Chicken")
    time.sleep(2)
    driver.find_element(By.NAME, "price").send_keys("2000")
    time.sleep(2)

    image_path = r'C:\Users\CNT\Desktop\FriedRice&Chicken.jpg'
    driver.find_element(By.NAME, "image").send_keys(image_path)    
    time.sleep(2)
    driver.find_element(By.NAME, "description").send_keys("This is a delicious dish that provide joy to its consumers after consumption.")
    time.sleep(2)

    # Submit the form
    driver.find_element(By.ID, "submit").click()

    # Verify product upload success
    assert "Product uploaded successfully" in driver.page_source
