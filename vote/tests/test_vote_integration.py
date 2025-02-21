import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

# Definir la URL del servicio vote según entorno
VOTE_URL = os.getenv("VOTE_URL", "http://localhost:5000")  # Usa localhost si no se especifica

@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()  # Definir opciones antes de usarlas
    chrome_options.add_argument("--headless")  # Para ejecutar en modo sin interfaz gráfica
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")

    # Configurar el WebDriver para conectarse al contenedor de Selenium
    driver = webdriver.Remote(
        command_executor='http://selenium:4444/wd/hub',  # URL del servicio Selenium en GitHub Actions
        options=chrome_options
    )
    yield driver
    driver.quit()

def test_title(driver):
    driver.get("http://localhost:80")
    assert "Vote" in driver.title  

def test_element(driver):
    driver.get("http://localhost:80")
    element = driver.find_element(By.ID, "vote-button") 
    assert element.is_displayed()







#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager
#import pytest

#@pytest.fixture
#def driver():
#    service = Service(ChromeDriverManager().install())
#    driver = webdriver.Chrome(service=service)
#    yield driver
#    driver.quit()

#def test_title(driver):
#    driver.get("http://localhost:5000")  # Cambiar por el servicio correcto
#    assert "Vote" in driver.title  # Ajustar según el título real de la página

#def test_element(driver):
#    driver.get("http://localhost:5000")
#    element = driver.find_element(By.ID, "vote-button")  # Asegúrate de que este ID existe
#    assert element.is_displayed()
