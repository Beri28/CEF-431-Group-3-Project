import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options


@pytest.fixture(scope="function")
def setup_driver():
    options = Options()
    # Uncomment the line below for headless mode
    # options.add_argument("--headless")
    
    with webdriver.Edge(options=options, service=Service()) as driver:
        yield driver


def test_add_koki_to_cart(setup_driver):
    driver = setup_driver
    driver.implicitly_wait(10)  # Set a default wait time

    try:
        driver.get("https://dreamland-restaurant.onrender.com/login")
        print("Navigated to login page.")

        driver.find_element(By.NAME, "email").send_keys("test@gmail.com")
        driver.find_element(By.NAME, "password").send_keys("12345")
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        print("Logged in.")

        # Wait for menu section
        menu_section = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#menu1"))
        )
        print("Menu section found.")

        # Validate cart count
        initial_count = int(driver.find_element(By.CSS_SELECTOR, ".shopping-cart .item-num").text)
        assert initial_count == 0, f"Initial cart count is not 0 (found: {initial_count})"

        # Locate Koki and add to cart
        menu_items = driver.find_elements(By.CSS_SELECTOR, "#menu1 .col-lg-3")
        koki_found = False

        for item in menu_items:
            food_name = item.find_element(By.CSS_SELECTOR, ".food-info p:first-child").text
            if food_name == "Koki":
                koki_found = True
                print("Koki is displayed in the menu section.")

                add_to_cart_button = item.find_element(By.CSS_SELECTOR, ".add-2-cart")
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_to_cart_button)
                WebDriverWait(driver, 5).until(EC.element_to_be_clickable(add_to_cart_button)).click()
                print("Koki added to cart!")

                # Assert updated cart count
                updated_count = WebDriverWait(driver, 10).until(
                    lambda d: int(d.find_element(By.CSS_SELECTOR, ".shopping-cart .item-num").text)
                )
                assert updated_count == 1, f"Unexpected cart count: {updated_count}"
                print("Test finished. Koki has been added to the cart.")
                return

        assert koki_found, "Koki is not displayed in the menu section."

    except Exception as e:
        pytest.fail(f"Test failed due to an exception: {e}")