from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

def test_email_input_presence_register(driver):
    try:
        driver.get("http://localhost:5000/register")
        email_input = driver.find_element(By.NAME, "email")
        assert email_input.is_displayed()
    except Exception as e:
        print(e)

def test_password_input_presence_register(driver):
    try:
        driver.get("http://localhost:5000/register")
        password_input = driver.find_element(By.NAME, "password")
        assert password_input.is_displayed()
    except Exception as e:
        print(e)

def test_username_input_presence(driver):
    try:
        driver.get("http://localhost:5000/register")
        name_input = driver.find_element(By.NAME, "name")
        assert name_input.is_displayed()
    except Exception as e:
        print(e)

def test_address_input_presence(driver):
    try:
        driver.get("http://localhost:5000/register")
        address_input = driver.find_element(By.NAME, "address")
        assert address_input.is_displayed()
    except Exception as e:
        print(e)

def test_contact_input_presence(driver):
    try:
        driver.get("http://localhost:5000/register")
        contact_input = driver.find_element(By.NAME, "contact")
        assert contact_input.is_displayed()
    except Exception as e:
        print(e)

def test_account_type_input_presence(driver):
    try:
        driver.get("http://localhost:5000/register")
        account_Type_input = driver.find_element(By.NAME, "account_Type")
        assert account_Type_input.is_displayed()
    except Exception as e:
        print(e)

def test_register_button_presence(driver):
    try:
        driver.get("http://localhost:5000/register")
        login_button = driver.find_element(By.ID, "register")
        assert login_button.is_displayed()
    except Exception as e:
        print(e)

def test_successful_registration_as_customer(driver):
    try:
        # Find and fill the signup form
        driver.get("http://localhost:5000/register")
        driver.find_element(By.NAME, "name").send_keys("john")
        time.sleep(2)
        email_input = driver.find_element(By.NAME, "email")
        email_input.send_keys("john@gmail.com")
        time.sleep(2)
        driver.find_element(By.NAME, "address").send_keys("molyko")
        time.sleep(2)
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys("12345678")
        time.sleep(2)
        driver.find_element(By.NAME, "contact").send_keys("680124356")
        time.sleep(2)
        driver.find_element(By.NAME, "account_Type").send_keys("restaurant-manager")
        time.sleep(2)
        submit_button = driver.find_element(By.ID, "register")
        submit_button.click()
        time.sleep(5)
        # WebDriverWait(driver, 10).until(EC.alert_is_present())
        # alert = driver.switch_to.alert
        # assert "userAccount" in driver.current_url
        assert "Welcome john" in driver.page_source
        # alert.accept()
    except Exception as e:
        print(e)

time.sleep(5)

def test_email_input_presence_login(driver):
    try:
        driver.get("http://localhost:5000/login")
        email_input = driver.find_element(By.NAME, "email")
        assert email_input.is_displayed()
    except Exception as e:
        print(e)

def test_password_input_presence_login(driver):
    try:
        driver.get("http://localhost:5000/login")
        password_input = driver.find_element(By.NAME, "password")
        assert password_input.is_displayed()
    except Exception as e:
        print(e)

def test_login_button_presence(driver):
    try:
        driver.get("http://localhost:5000/login")
        login_button = driver.find_element(By.ID, "login")
        assert login_button.is_displayed()
    except Exception as e:
        print(e)

def test_successful_add_to_todays_menu(driver):
    try:
        driver.get("http://localhost:5000/login")
        email_input = driver.find_element(By.NAME, "email")
        password_input = driver.find_element(By.NAME, "password")
        submit_button = driver.find_element(By.ID, "login")
        email_input.send_keys("bongyu@gmail.com")
        password_input.send_keys("12345678")
        submit_button.click()
        time.sleep(3)
        add_to_todays_menu = driver.find_elements(By.CLASS_NAME, "todays-menu")
        r_add_to_todays_menu = driver.find_elements(By.CLASS_NAME, "r-todays-menu")
        print(add_to_todays_menu[1])
        print("////////////////////")
        for i,element in enumerate(add_to_todays_menu):
            if "d-none" in element.get_attribute("class"):
                r_add_to_todays_menu[i].click()
                time.sleep(2)
                # assert "d-none" in r_add_to_todays_menu[i].get_attribute("class")
            elif "d-none" not in element.get_attribute("class") :
                element.click()
                time.sleep(2)
                # assert "d-none" in element.get_attribute("class")
            else:
                raise AssertionError("Test failed. Couldn't find button")
        time.sleep(2)
    except Exception as e:
        print(e)
def test_successful_login(driver):
    try:
        driver.get("http://localhost:5000/login")
        email_input = driver.find_element(By.NAME, "email")
        password_input = driver.find_element(By.NAME, "password")
        submit_button = driver.find_element(By.ID, "login")
        email_input.send_keys("john@gmail.com")
        password_input.send_keys("12345678")
        submit_button.click()
        time.sleep(5)
        # WebDriverWait(driver, 10).until(EC.alert_is_present())
        # alert = driver.switch_to.alert
        assert "Hello John" in driver.page_source
        # alert.accept()
    except Exception as e:
        print(e)

