import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, WebDriverException
import pytest

URL = "http://localhost:5000/"
EMAIL = "bongyu@gmail.com"
PASSWORD = "12345678"
NEW_PRICE = "10000"
NEW_DESCRIPTION = "Edited description"

def test_successful_registration_as_customer(driver):
    try:
        wait = WebDriverWait(driver, 10)
        # Find and fill the signup form
        driver.get(URL+"register")
        driver.find_element(By.NAME, "name").send_keys("Jane")
        time.sleep(2)
        email_input = driver.find_element(By.NAME, "email")
        email_input.send_keys("Jane@gmail.com")
        time.sleep(2)
        driver.find_element(By.NAME, "address").send_keys("molyko")
        time.sleep(2)
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys("12345678")
        time.sleep(2)
        driver.find_element(By.NAME, "contact").send_keys("680124356")
        time.sleep(2)
        # driver.find_element(By.NAME, "account_Type").send_keys("restaurant-manager")
        wait.until(EC.element_to_be_clickable((By.NAME, "account_Type"))).send_keys("customer")
        time.sleep(2)
        submit_button = driver.find_element(By.ID, "register")
        driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        submit_button.click()
        time.sleep(5)
        # WebDriverWait(driver, 10).until(EC.alert_is_present())
        # alert = driver.switch_to.alert
        # assert "userAccount" in driver.current_url
        assert "/userAccount" in driver.current_url
        print("✅ Successful register as manager")
        time.sleep(5)
    except Exception as e:
        pytest.fail(f"❌ Error registering manager: {str(e)}")

def test_customer_flow(driver):
    try:
        wait = WebDriverWait(driver, 10)
        driver.get(URL+"login")
        email_input = driver.find_element(By.NAME, "email")
        password_input = driver.find_element(By.NAME, "password")
        submit_button = driver.find_element(By.ID, "login")
        email_input.send_keys("Jane@gmail.com")
        password_input.send_keys("12345678")
        submit_button.click()
        print("✅ Successful login")

        time.sleep(2)

        # Validate cart count
        initial_count = int(driver.find_element(By.CSS_SELECTOR, ".shopping-cart .item-num").text)
        print(initial_count)
        assert initial_count == 0, f"Initial cart count is not 0 (found: {initial_count})"

        # Locate Koki and add to cart
        menu_items = driver.find_elements(By.CLASS_NAME, "food-info")
        koki_found = False
        for item in menu_items:
            time.sleep(2)
            food_name = item.find_element(By.CSS_SELECTOR, ".food-info p:first-child").text
            if food_name == "Koki":
                koki_found = True
                print("Koki is displayed in the menu section.")
                add_to_cart_button = item.find_element(By.CSS_SELECTOR, ".add-2-cart")
                driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_button)
                time.sleep(1)
                add_to_cart_button.click()
                time.sleep(1)
                print("Koki added to cart!")

                updated_count = WebDriverWait(driver, 10).until(
                    lambda d: int(d.find_element(By.CSS_SELECTOR, ".shopping-cart .item-num").text)
                )
                assert updated_count == 1, f"Unexpected cart count: {updated_count}"
                print("Koki has been added to the cart.")
        assert koki_found, "Koki is not displayed in the menu section."
        print("✅ Added to cart")
        cart=driver.find_element(By.CSS_SELECTOR, ".shopping-cart .item-num")
        driver.execute_script("arguments[0].scrollIntoView(true);", cart)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".shopping-cart .item-num"))).click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "payment"))).click()
        time.sleep(1)
        driver.find_element(By.NAME,"momo-number").send_keys('670123451')
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "modal-trigger"))).click()
        assert "Beware" in driver.page_source
        print("✅ Payment required")
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "close"))).click()
        time.sleep(2)
        home = driver.find_element(By.CLASS_NAME, "fa-home").click()
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, "Home").click()
        time.sleep(4)
        # Ensure dropdown menu is clickable and open
        more = driver.find_element(By.CLASS_NAME, "logout")
        driver.execute_script("arguments[0].scrollIntoView(true);", more)
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "logout"))).click()
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, "Logout").click()
        time.sleep(2)
        print("✅ Clicked logout link")
        try:
            WebDriverWait(driver, 10).until(EC.url_contains("/"))
            print("✅ Logout successful! Navigated to home page.")
        except TimeoutException:
            pytest.fail("❌ Logout failed: URL didn't change to home page")
    except Exception as e:
        pytest.fail(f"❌ Error Testing admin flow: {str(e)}")

def test_search(driver):
    # Navigate to the local login page
    driver.get(URL)  # Update as necessary

    # Perform login
    # email_input = driver.find_element(By.NAME, 'email')
    # email_input.send_keys('john@gmail.com')
    #
    # password_input = driver.find_element(By.NAME, 'password')
    # password_input.send_keys('12345678')
    #
    # login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    # login_button.click()

    # Wait for the page to load
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, 'search')))

    # Perform search
    search_input = driver.find_element(By.NAME, 'search')
    search_input.send_keys('Achombo')

    search_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    search_button.click()

    # Wait for search results
    WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.row.w-100 .col-lg-3')))
    time.sleep(2)
    # Validate search results
    results = driver.find_elements(By.CSS_SELECTOR, '.row.w-100 .col-lg-3')
    time.sleep(2)
    print("✅ Email input present")
    assert results, pytest.fail(f"❌ Error finding meal")
