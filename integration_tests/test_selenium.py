from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configurar ChromeDriver automáticamente
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Abrir la página de prueba
driver.get("https://www.google.com")
print("Título de la página:", driver.title)

driver.quit()
 
