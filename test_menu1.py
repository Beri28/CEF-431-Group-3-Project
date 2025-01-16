import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuration
EDGE_DRIVER_PATH = "C:/WebDrivers/msedgedriver.exe"  # Ensure this path is correct
URL = "https://dreamland-restaurant.onrender.com/login"
EMAIL = "chuyeprincelytata@gmail.com"
PASSWORD = "1234"
NEW_PRICE = "10000"
NEW_DESCRIPTION = "Edited description"

def pytest_html_report_title(report):
    report.title = "Menu Editing Test Report"

@pytest.fixture(scope="function")
def driver(request):
    """Fixture to set up and tear down the WebDriver."""
    service = Service(EDGE_DRIVER_PATH)
    driver = webdriver.Edge(service=service)
    driver.maximize_window()

    def teardown():
        """Tear down WebDriver."""
        driver.quit()

    request.addfinalizer(teardown)
    return driver

class TestMenuEditing:
    def scroll_and_find_edit_button(self, driver, wait):
        """Scroll through the page and find the 'Edit' button."""
        try:
            # Scroll to promo section first
            driver.execute_script("document.querySelector('.todays-promo-user').scrollIntoView(true);")
            time.sleep(2)

            # Try mobile view first
            buttons = driver.find_elements(By.CSS_SELECTOR, ".carousel-food-info button.btn-outline-orange-2")
            for button in buttons:
                if button.text.strip().lower() == 'edit':
                    return button

            # Try desktop view
            buttons = driver.find_elements(By.CSS_SELECTOR, ".food-info button.btn-outline-orange-2")
            for button in buttons:
                if button.text.strip().lower() == 'edit':
                    return button

            # Progressive scroll if button not found
            total_height = driver.execute_script("return document.body.scrollHeight")
            current_position = 0
            scroll_step = 300

            while current_position < total_height:
                current_position += scroll_step
                driver.execute_script(f"window.scrollTo(0, {current_position});")
                time.sleep(1)

                buttons = driver.find_elements(By.CSS_SELECTOR, "button.btn-outline-orange-2")
                for button in buttons:
                    if button.text.strip().lower() == 'edit':
                        return button

            return None
        except Exception as e:
            print(f"Error while searching for edit button: {str(e)}")
            return None

    def update_meal_details(self, driver, wait):
        """Update the meal price and description."""
        try:
            modal = wait.until(EC.presence_of_element_located((By.ID, "exampleModalCenteredScrollable")))
            time.sleep(2)

            # Update price
            price_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='price']")))
            price_field.clear()
            price_field.send_keys(NEW_PRICE)

            # Update description
            description_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[name='description']")))
            description_field.clear()
            description_field.send_keys(NEW_DESCRIPTION)

            # Click the final 'Edit' button
            final_edit_button = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "input[type='submit'][value='Edit']")
            ))

            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", final_edit_button)
            time.sleep(1)

            try:
                final_edit_button.click()
                wait.until(EC.invisibility_of_element_located((By.ID, "exampleModalCenteredScrollable")))
                return True
            except:
                driver.execute_script("arguments[0].click();", final_edit_button)
                return True
        except Exception as e:
            print(f"Error while updating meal details: {str(e)}")
            return False

    def test_edit_menu_item(self, driver):
        """Test case for editing a menu item."""
        wait = WebDriverWait(driver, 20)

        try:
            # Navigate to the website
            driver.get(URL)
            time.sleep(5)

            # Login process
            email_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email']")))
            email_field.send_keys(EMAIL)

            password_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']")))
            password_field.send_keys(PASSWORD)

            login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
            login_button.click()

            time.sleep(5)

            # Find and click the 'Edit' button
            edit_button = self.scroll_and_find_edit_button(driver, wait)
            assert edit_button is not None, "Edit button not found"

            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", edit_button)
            time.sleep(1)
            edit_button.click()

            # Update meal details
            assert self.update_meal_details(driver, wait), "Failed to update meal details"

            time.sleep(2)

        except Exception as e:
            pytest.fail(f"Test failed due to an exception: {str(e)}", pytrace=True)

if __name__ == "__main__":
    pytest.main(["-v", "--html=test_reports/menu_test_report.html", "--self-contained-html"]) 
