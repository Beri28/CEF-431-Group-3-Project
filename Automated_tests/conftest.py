import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep

# @pytest.fixture(scope="session")
# def driver():
#     options = webdriver.ChromeOptions()
#     options.add_argument("--no-sandbox")
#     chrome_service = ChromeService(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=chrome_service, options=options)
#     yield driver
#     sleep(2)
#     driver.quit()

@pytest.fixture
def driver():
    driver = webdriver.Edge()  # or any other browser
    yield driver
    driver.quit()
