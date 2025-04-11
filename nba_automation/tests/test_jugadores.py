from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup del driver
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
service = Service("C:/Users/micha/Desktop/tarea4_prueba/nba_automation/tests/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

# Ir a la página de NBA
driver.get("https://www.nba.com")

# Aceptar cookies si aparece
try:
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'I Accept')]"))
    ).click()
    print("✅ Cookies aceptadas")
except:
    print("⚠️ No apareció el botón de cookies o ya estaba aceptado")

# Ir a la sección Players
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Players"))
).click()
print("🧍‍♂️ Sección 'Players' abierta")

# Esperar que cargue la tabla
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "table"))
)

# Buscar a Stephen Curry
search_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Search Players']"))
)
search_input.clear()
search_input.send_keys("Stephen Curry")
print("🔍 Buscando a Stephen Curry")

time.sleep(10)  # Esperar para ver resultados

# Volver a cargar página para limpiar búsqueda
driver.get("https://www.nba.com/players")

# Esperar que cargue la tabla
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "table"))
)

# Buscar a LeBron James
search_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Search Players']"))
)
search_input.clear()
search_input.send_keys("LeBron James")
print("🔍 Buscando a LeBron James")

time.sleep(10)  # Esperar para ver resultados

# Esperar que el usuario vea resultados antes de cerrar
input("Presiona ENTER para cerrar el navegador...")

# Cerrar navegador
driver.quit()

