from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy, ProxyType
import os
import pytest

@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # Para que no se abra una ventana de navegador
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # URL del servicio Selenium
    selenium_url = "http://selenium:4444/wd/hub"

    driver = webdriver.Remote(
        command_executor=selenium_url,
        options=chrome_options
    )
    yield driver
    driver.quit()

def test_title(driver):
    driver.get("http://www.google.com")
    assert "Google" in driver.title