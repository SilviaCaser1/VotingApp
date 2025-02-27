from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_title(driver):
    driver.get("http://localhost:5051")  # Cambiar por el servicio correcto
    assert "Vote" in driver.title  # Ajustar según el título real de la página

def test_element(driver):
    driver.get("http://localhost:5051")
    element = driver.find_element(By.ID, "vote-button")  # Asegúrate de que este ID existe
    assert element.is_displayed()
