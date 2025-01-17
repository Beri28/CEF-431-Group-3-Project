import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    """Set up the WebDriver for each test."""
    options = Options()
    service = Service('C:\Program Files\edgedriver_win64/msedgedriver.exe')  # Replace with actual path
    driver = webdriver.Edge(service=service, options=options)
    yield driver
    driver.quit()

def test_login_and_search(driver):
    # Navigate to the local login page
    driver.get('https://dreamland-restaurant.onrender.com/login')  # Update as necessary
   
    # Perform login
    email_input = driver.find_element(By.NAME, 'email')
    email_input.send_keys('test@gmail.com')
   
    password_input = driver.find_element(By.NAME, 'password')
    password_input.send_keys('12345')
   
    login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    login_button.click()
   
    # Wait for the page to load
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, 'search')))
   
    # Perform search
    search_input = driver.find_element(By.NAME, 'search')
    search_input.send_keys('Achombo')
   
    search_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    search_button.click()
   
    # Wait for search results
    WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.row.w-100 .col-lg-3')))
   
    # Validate search results
    results = driver.find_elements(By.CSS_SELECTOR, '.row.w-100 .col-lg-3')
    assert results, "Search results not found"
