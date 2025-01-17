import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
import time

@pytest.fixture(scope="function")
def setup_browser():
    """Fixture to set up and tear down the Selenium WebDriver."""
    options = webdriver.EdgeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--ignore-certificate-errors')
    
    driver = None
    try:
        driver = webdriver.Edge(options=options)
        wait = WebDriverWait(driver, 10)
        actions = ActionChains(driver)
        yield driver, wait, actions  # Provide the driver, wait, and actions to the test
    except WebDriverException as e:
        pytest.fail(f"❌ WebDriver initialization failed: {str(e)}")
    finally:
        if driver:
            print("🔄 Closing the browser...")
            driver.quit()


def wait_and_click(driver, wait, by, selector, message):
    """Helper function to wait for and click elements."""
    try:
        element = wait.until(EC.element_to_be_clickable((by, selector)))
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)  # Small pause after scrolling
        driver.execute_script("arguments[0].click();", element)
        print(f"✅ {message}")
    except Exception as e:
        pytest.fail(f"❌ Error clicking element {selector}: {str(e)}")


def test_user_account_login_logout(setup_browser):
    """Test case for logging in and logging out."""
    driver, wait, actions = setup_browser

    # Step 1: Open the login page
    print("🔄 Opening the login page...")
    try:
        driver.get("https://dreamland-restaurant.onrender.com/userAccount")
    except Exception as e:
        pytest.fail(f"❌ Failed to open login page: {str(e)}")
    
    # Step 2: Fill in login credentials
    print("🔄 Filling in login credentials...")
    try:
        email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        email_input.clear()
        password_input.clear()
        email_input.send_keys("princelychuye@gmail.com")
        password_input.send_keys("1234567")

        # Click the login button
        wait_and_click(driver, wait, By.XPATH, "//button[contains(text(), 'Login')]", "Login button clicked")
    except Exception as e:
        pytest.fail(f"❌ Error during login: {str(e)}")
    
    # Verify login by checking URL
    print("\n🔄 Verifying login...")
    try:
        wait.until(EC.url_contains("/userAccount"))
        print("✅ Login successful!")
    except TimeoutException:
        pytest.fail("❌ Login failed: URL didn't change as expected")

    # Step 3: Handle the dropdown for logout
    print("🔄 Handling dropdown for logout...")
    try:
        dropdown_container = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".user-nav-menu .dropdown")))

        # Ensure dropdown menu is clickable and open
        dropdown_trigger = dropdown_container.find_element(By.CSS_SELECTOR, ".fa-align-justify")
        dropdown_menu = dropdown_container.find_element(By.CSS_SELECTOR, ".dropdown-menu")
        
        # Click dropdown trigger
        driver.execute_script("arguments[0].click();", dropdown_trigger)
        time.sleep(0.5)
        
        # Click logout link
        logout_link = dropdown_menu.find_element(By.CSS_SELECTOR, "a[href='/logout']")
        driver.execute_script("arguments[0].click();", logout_link)
        print("✅ Clicked logout link")
    except Exception as e:
        pytest.fail(f"❌ Error during logout: {str(e)}")

    # Verify logout by checking URL (should go to the home page, not login page)
    print("\n🔄 Verifying logout...")
    try:
        wait.until(EC.url_contains("/"))
        print("✅ Logout successful! Navigated to home page.")
    except TimeoutException:
        pytest.fail("❌ Logout failed: URL didn't change to home page")
