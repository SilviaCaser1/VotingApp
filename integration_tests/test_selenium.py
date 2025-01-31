import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import tempfile

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Modo sin interfaz gráfica (ideal para CI/CD)
    chrome_options.add_argument("--no-sandbox")  # Requerido en entornos sin UI
    chrome_options.add_argument("--disable-dev-shm-usage")  # Previene problemas de memoria en contenedores
    chrome_options.add_argument("--disable-gpu")  # Desactiva GPU, útil para headless en Linux
    chrome_options.add_argument("--user-data-dir=/tmp/chrome-user-data")  # Usa un directorio único
    chrome_options.add_argument("--remote-debugging-port=9222")  # Evita conflicto con depuración

    # Configurar el driver de Chrome
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    yield driver
    driver.quit()
