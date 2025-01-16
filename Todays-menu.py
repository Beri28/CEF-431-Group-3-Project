from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_successful_add_to_or_remove_from_todays_menu(driver):
    try:
        driver.get("http://localhost:5000/login")
        email_input = driver.find_element(By.NAME, "email")
        password_input = driver.find_element(By.NAME, "password")
        submit_button = driver.find_element(By.ID, "login")
        email_input.send_keys("bongyu@gmail.com")
        password_input.send_keys("12345678")
        submit_button.click()
        time.sleep(3)
        add_to_todays_menu = driver.find_element(By.CLASS_NAME, "todays-menu")
        r_add_to_todays_menu = driver.find_element(By.CLASS_NAME, "r-todays-menu")
        if "d-none" in add_to_todays_menu.get_attribute("class"):
            r_add_to_todays_menu.click()
            time.sleep(2)
            # assert "d-none" in r_add_to_todays_menu[i].get_attribute("class")
        elif "d-none" not in add_to_todays_menu.get_attribute("class") :
            add_to_todays_menu.click()
            time.sleep(2)
            # assert "d-none" in element.get_attribute("class")
        else:
            raise AssertionError("Test failed. Couldn't find button")
        time.sleep(2)
    except Exception as e:
        print(e)