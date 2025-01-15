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
