import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@pytest.fixture(scope="session")
def driver():
    selenium_url = "http://host.docker.internal:4444/wd/hub"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Espera a que Selenium esté listo antes de conectarse
    max_attempts = 10
    for attempt in range(max_attempts):
        try:
            driver = webdriver.Remote(
                command_executor=selenium_url,
                options=chrome_options
            )
            break  # Si se conecta correctamente, salimos del bucle
        except Exception as e:
            print(f"Intento {attempt+1}/{max_attempts} fallido: {e}")
            time.sleep(5)  # Esperamos antes de intentar de nuevo
    else:
        raise RuntimeError("Selenium no está disponible después de varios intentos.")

    yield driver
    driver.quit()
