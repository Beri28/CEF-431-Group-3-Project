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

URL = "http://localhost:5000/login"
EMAIL = "bongyu@gmail.com"
PASSWORD = "12345678"
NEW_PRICE = "10000"
NEW_DESCRIPTION = "Edited description"


def test_email_input_presence_register(driver):
    try:
        driver.get("http://localhost:5000/register")
        email_input = driver.find_element(By.NAME, "email")
        assert email_input.is_displayed()
        print("✅ Email input present")
    except Exception as e:
        pytest.fail(f"❌ Error finding email input: {str(e)}")

def test_password_input_presence_register(driver):
    try:
        driver.get("http://localhost:5000/register")
        password_input = driver.find_element(By.NAME, "password")
        assert password_input.is_displayed()
        print("✅ Password input present")
    except Exception as e:
        pytest.fail(f"❌ Error finding password input: {str(e)}")

def test_username_input_presence(driver):
    try:
        driver.get("http://localhost:5000/register")
        name_input = driver.find_element(By.NAME, "name")
        assert name_input.is_displayed()
        print("✅ Username input present")
    except Exception as e:
        pytest.fail(f"❌ Error finding username input: {str(e)}")

def test_address_input_presence(driver):
    try:
        driver.get("http://localhost:5000/register")
        address_input = driver.find_element(By.NAME, "address")
        assert address_input.is_displayed()
        print("✅ Address input present")
    except Exception as e:
        pytest.fail(f"❌ Error finding address input: {str(e)}")

def test_contact_input_presence(driver):
    try:
        driver.get("http://localhost:5000/register")
        contact_input = driver.find_element(By.NAME, "contact")
        assert contact_input.is_displayed()
        print("✅ Contact input present")
    except Exception as e:
        pytest.fail(f"❌ Error finding contact input: {str(e)}")

def test_account_type_input_presence(driver):
    try:
        driver.get("http://localhost:5000/register")
        account_Type_input = driver.find_element(By.NAME, "account_Type")
        assert account_Type_input.is_displayed()
        print("✅ Account type input present")
    except Exception as e:
        pytest.fail(f"❌ Error finding account type input: {str(e)}")

def test_register_button_presence(driver):
    try:
        driver.get("http://localhost:5000/register")
        login_button = driver.find_element(By.ID, "register")
        assert login_button.is_displayed()
        print("✅ Register button present")
    except Exception as e:
        pytest.fail(f"❌ Error finding register button: {str(e)}")

def test_successful_registration_as_customer(driver):
    try:
        wait = WebDriverWait(driver, 10)
        # Find and fill the signup form
        driver.get("http://localhost:5000/register")
        driver.find_element(By.NAME, "name").send_keys("John")
        time.sleep(2)
        email_input = driver.find_element(By.NAME, "email")
        email_input.send_keys("john2@gmail.com")
        time.sleep(2)
        driver.find_element(By.NAME, "address").send_keys("molyko")
        time.sleep(2)
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys("12345678")
        time.sleep(2)
        driver.find_element(By.NAME, "contact").send_keys("680124356")
        time.sleep(2)
        driver.find_element(By.NAME, "account_Type").send_keys("customer")
        time.sleep(2)
        # submit_button = driver.find_element(By.ID, "register")
        submit_button = wait.until(EC.element_to_be_clickable((By.ID, "register")))
        submit_button.click()
        time.sleep(6)
        # WebDriverWait(driver, 10).until(EC.alert_is_present())
        # alert = driver.switch_to.alert
        # assert "userAccount" in driver.current_url
        assert "/userAccount" in driver.current_url
        # alert.accept()
        print("✅ Successful register as customer")
        time.sleep(5)
    except Exception as e:
        pytest.fail(f"❌ Error registering customer: {str(e)}")

def test_successful_registration_as_manager(driver):
    try:
        wait = WebDriverWait(driver, 10)
        # Find and fill the signup form
        driver.get("http://localhost:5000/register")
        driver.find_element(By.NAME, "name").send_keys("Mary")
        time.sleep(2)
        email_input = driver.find_element(By.NAME, "email")
        email_input.send_keys("mary@gmail.com")
        time.sleep(2)
        driver.find_element(By.NAME, "address").send_keys("molyko")
        time.sleep(2)
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys("12345678")
        time.sleep(2)
        driver.find_element(By.NAME, "contact").send_keys("680124356")
        time.sleep(2)
        # driver.find_element(By.NAME, "account_Type").send_keys("restaurant-manager")
        wait.until(EC.element_to_be_clickable((By.NAME, "account_Type"))).send_keys("restaurant-manager")
        time.sleep(2)
        submit_button = driver.find_element(By.ID, "register")
        submit_button.click()
        driver.find_element(By.NAME, "code").send_keys("Mary4321")
        # driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))).click()
        time.sleep(5)
        # WebDriverWait(driver, 10).until(EC.alert_is_present())
        # alert = driver.switch_to.alert
        # assert "userAccount" in driver.current_url
        assert "/userAccount2" in driver.current_url
        print("✅ Successful register as manager")
        time.sleep(5)
    except Exception as e:
        pytest.fail(f"❌ Error registering manager: {str(e)}")

def test_email_input_presence_login(driver):
    try:
        driver.get("http://localhost:5000/login")
        email_input = driver.find_element(By.NAME, "email")
        assert email_input.is_displayed()
        print("✅ Email input present")
    except Exception as e:
        pytest.fail(f"❌ Error finding email input: {str(e)}")

def test_password_input_presence_login(driver):
    try:
        driver.get("http://localhost:5000/login")
        password_input = driver.find_element(By.NAME, "password")
        assert password_input.is_displayed()
        print("✅ Password input present")
    except Exception as e:
        pytest.fail(f"❌ Error finding password input: {str(e)}")

def test_login_button_presence(driver):
    try:
        driver.get("http://localhost:5000/login")
        login_button = driver.find_element(By.ID, "login")
        assert login_button.is_displayed()
        print("✅ Login button present")
    except Exception as e:
        pytest.fail(f"❌ Error finding login button: {str(e)}")

def test_successful_login(driver):
    try:
        driver.get("http://localhost:5000/login")
        email_input = driver.find_element(By.NAME, "email")
        password_input = driver.find_element(By.NAME, "password")
        submit_button = driver.find_element(By.ID, "login")
        email_input.send_keys("bongyu@gmail.com")
        password_input.send_keys("12345678")
        submit_button.click()
        time.sleep(5)
        # WebDriverWait(driver, 10).until(EC.alert_is_present())
        # alert = driver.switch_to.alert
        assert "Hello Bongyu" in driver.page_source
        print("✅ Successful login")
    except Exception as e:
        pytest.fail(f"❌ Error logging In: {str(e)}")

def test_admin_upload_meal(driver):
    try:
        driver.get("http://localhost:5000/login")
        email_input = driver.find_element(By.NAME, "email")
        password_input = driver.find_element(By.NAME, "password")
        submit_button = driver.find_element(By.ID, "login")
        email_input.send_keys("bongyu@gmail.com")
        password_input.send_keys("12345678")
        submit_button.click()
        time.sleep(3)
        add = driver.find_element(By.CLASS_NAME, "fa-plus-circle")
        add.click()
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, "Add to Todays menu").click()
        time.sleep(2)

        # Fill out the product upload form
        driver.find_element(By.NAME, "name").send_keys("Ndole")
        time.sleep(2)
        driver.find_element(By.NAME, "price").send_keys("5000")
        time.sleep(2)
        driver.find_element(By.NAME, "image").send_keys(os.getcwd()+'/assets/koki.jpg')
        time.sleep(2)
        driver.find_element(By.NAME, "description").send_keys(
            "This is a delicious dish that provide joy to its consumers after consumption.")
        time.sleep(2)
        # Submit the form
        driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
        time.sleep(3)

        # Verify product upload success
        assert "/userAccount2" in driver.current_url
        print("✅ Added new meal")
    except Exception as e:
        pytest.fail(f"❌ Error adding meal: {str(e)}")

def test_search(driver):
    # Navigate to the local login page
    driver.get('http://localhost:5000/')  # Update as necessary

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

def test_add_to_or_remove_from_todays_menu(driver):
    try:
        wait = WebDriverWait(driver, 10)
        driver.get("http://localhost:5000/login")
        email_input = driver.find_element(By.NAME, "email")
        password_input = driver.find_element(By.NAME, "password")
        submit_button = driver.find_element(By.ID, "login")
        email_input.send_keys("bongyu@gmail.com")
        password_input.send_keys("12345678")
        # submit_button.click()
        wait.until(EC.element_to_be_clickable((By.ID, "login"))).click()
        time.sleep(5)
        add_to_todays_menu = driver.find_element(By.CLASS_NAME, "todays-menu")
        time.sleep(5)
        r_add_to_todays_menu = driver.find_element(By.CLASS_NAME, "r-todays-menu")
        # for i, element in enumerate(add_to_todays_menu):
        if "d-none" in add_to_todays_menu.get_attribute("class"):
            time.sleep(3)
            r_add_to_todays_menu.click()
            time.sleep(5)
            # assert "d-none" in r_add_to_todays_menu[i].get_attribute("class")
        elif "d-none" not in add_to_todays_menu.get_attribute("class"):
            time.sleep(3)
            # add_to_todays_menu.click()
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "todays-menu"))).click()
            time.sleep(5)
            # assert "d-none" in element.get_attribute("class")
        else:
            raise AssertionError("Test failed. Couldn't find button")
        time.sleep(2)
        print("✅ Edited menu of the day")
    except Exception as e:
        pytest.fail(f"❌ Error editing menu of the day: {str(e)}")

def test_add_to_or_remove_from_promo_menu(driver):
    try:
        driver.get("http://localhost:5000/login")
        email_input = driver.find_element(By.NAME, "email")
        password_input = driver.find_element(By.NAME, "password")
        submit_button = driver.find_element(By.ID, "login")
        email_input.send_keys("bongyu@gmail.com")
        password_input.send_keys("12345678")
        submit_button.click()
        time.sleep(3)
        add_to_todays_menu = driver.find_element(By.CLASS_NAME, "promo-menu")
        time.sleep(2)
        r_add_to_todays_menu = driver.find_element(By.CLASS_NAME, "r-promo-menu")
        if "d-none" in add_to_todays_menu.get_attribute("class"):
            time.sleep(3)
            r_add_to_todays_menu.click()
            time.sleep(2)
            # assert "d-none" in r_add_to_todays_menu[i].get_attribute("class")
        elif "d-none" not in add_to_todays_menu.get_attribute("class") :
            time.sleep(3)
            add_to_todays_menu.click()
            time.sleep(2)
            # assert "d-none" in element.get_attribute("class")
        else:
            raise AssertionError("Test failed. Couldn't find button")
        time.sleep(2)
        print("✅ Edited promo menu")
    except Exception as e:
        pytest.fail(f"❌ Error editing promo menu: {str(e)}")

def test_add_koki_to_cart(driver):
    driver.implicitly_wait(10)  # Set a default wait time

    try:
        driver.get("http://localhost:5000/login")
        print("Navigated to login page.")

        driver.find_element(By.NAME, "email").send_keys("bongyu@gmail.com")
        driver.find_element(By.NAME, "password").send_keys("12345678")
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        print("Logged in.")
        # driver.find_element(By.CLASS_NAME, "add-2-cart").click()
        time.sleep(4)

        # Validate cart count
        initial_count = int(driver.find_element(By.CSS_SELECTOR, ".shopping-cart .item-num").text)
        print(initial_count)
        assert initial_count == 0, f"Initial cart count is not 0 (found: {initial_count})"

        # Locate Koki and add to cart
        menu_items = driver.find_elements(By.CLASS_NAME, "food-info")
        koki_found = False
        for item in menu_items:
            time.sleep(4)
            food_name = item.find_element(By.CSS_SELECTOR, ".food-info p:first-child").text
            if food_name == "Koki":
                koki_found = True
                print("Koki is displayed in the menu section.")
                add_to_cart_button = WebDriverWait(driver, 10).until(item.find_element(By.CSS_SELECTOR, ".add-2-cart"))
                add_to_cart_button.click()
                time.sleep(6)
                print("Koki added to cart!")

                updated_count = WebDriverWait(driver, 10).until(
                    lambda d: int(d.find_element(By.CSS_SELECTOR, ".shopping-cart .item-num").text)
                )
                assert updated_count == 1, f"Unexpected cart count: {updated_count}"
                print("Test finished. Koki has been added to the cart.")
                return
        assert koki_found, "Koki is not displayed in the menu section."
        print("✅ Added to cart")
    except Exception as e:
        pytest.fail(f"❌ Error adding to cart: {str(e)}")

class TestMealEditing:
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

            # Update photo
            image_field=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"input[name='image']")))
            image_field.send_keys(os.getcwd()+'/assets/koki.jpg')

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
                time.sleep(10)
                wait.until(EC.invisibility_of_element_located((By.ID, "exampleModalCenteredScrollable")))
                return True
            except:
                driver.execute_script("arguments[0].click();", final_edit_button)
                return True
        except Exception as e:
            print(f"Error while updating meal details: {str(e)}")
            return False

    def test_edit_meal_item(self, driver):
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
            print("✅ Meal Edited")
        except Exception as e:
            pytest.fail(f"❌ Error editing meal: {str(e)}")

def test_logout(driver):
    try:
        driver.get("http://localhost:5000/login")
        email_input = driver.find_element(By.NAME, "email")
        password_input = driver.find_element(By.NAME, "password")
        submit_button = driver.find_element(By.ID, "login")
        email_input.send_keys("bongyu@gmail.com")
        password_input.send_keys("12345678")
        submit_button.click()
        time.sleep(5)
        # dropdown_container =wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".user-nav-menu .dropdown")))
        dropdown_container=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".user-nav-menu .dropdown")))

        # Ensure dropdown menu is clickable and open
        more = driver.find_element(By.CLASS_NAME, "more")
        more.click()
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, "Logout").click()
        time.sleep(2)
        print("✅ Clicked logout link")
    except Exception as e:
        pytest.fail(f"❌ Error during logout: {str(e)}")

    # Verify logout by checking URL (should go to the home page, not login page)
    print("\n🔄 Verifying logout...")
    try:
        WebDriverWait(driver, 10).until(EC.url_contains("/"))
        print("✅ Logout successful! Navigated to home page.")
    except TimeoutException:
        pytest.fail("❌ Logout failed: URL didn't change to home page")
