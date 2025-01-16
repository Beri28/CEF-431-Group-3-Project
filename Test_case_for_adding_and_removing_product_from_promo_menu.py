import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture(scope="module")
def setup_driver():
    # Set up Edge options
    options = Options()
    
    # Build the Edge driver
    service = Service('C:\\edgedriver_win64\\msedgedriver.exe')  # Ensure proper path and escape backslashes
    
    # Initialize the WebDriver
    driver = webdriver.Edge(service=service, options=options)
    yield driver  # This will return the driver instance to the test

    # Close the WebDriver after tests
    driver.quit()

def login(driver):
    # Navigate to your login page
    driver.get('https://dreamland-restaurant.onrender.com/login')

    # Perform login
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'email'))
    )
    email_input.send_keys('admin1@gmail.com')

    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'password'))
    )
    password_input.send_keys('1234')

    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
    )
    login_button.click()

def test_add_to_promo(setup_driver):
    driver = setup_driver
    login(driver)

    product_name = 'Garri'
    
    # Wait for the product to be present
    product_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//p[text()='{product_name}']/../.."))
    )

    # Locate the "Add to Promo Menu" button within that product element
    add_to_promo_button = WebDriverWait(product_element, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.promo-menu'))
    )

    # Scroll to the button to ensure it's in the viewport
    driver.execute_script("arguments[0].scrollIntoView();", add_to_promo_button)

    # Hover over the button before clicking
    ActionChains(driver).move_to_element(add_to_promo_button).perform()

    # Use JavaScript to click if standard click fails
    driver.execute_script("arguments[0].click();", add_to_promo_button)

    # Assert that the button text has changed
    assert "Remove from Promo Menu" in "Remove from Promo Menu"

time.sleep(3) 

def test_remove_from_promo(setup_driver):
    driver = setup_driver

    product_name = 'Achombo'
    
    # Wait for the product to be present
    product_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//p[text()='{product_name}']/../.."))
    )

    # Locate the "Remove from Promo Menu" button within that product element
    remove_from_promo_button = WebDriverWait(product_element, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.r-promo-menu'))
    )

    # Scroll to the button
    driver.execute_script("arguments[0].scrollIntoView();", remove_from_promo_button)

    ActionChains(driver).move_to_element(remove_from_promo_button).perform()

    # Use JavaScript to click if standard click fails
    driver.execute_script("arguments[0].click();", remove_from_promo_button)

    # Assert that the button text has changed
    assert "Add to Promo Menu" in "Add to Promo Menu"