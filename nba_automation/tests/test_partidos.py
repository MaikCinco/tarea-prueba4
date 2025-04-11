import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from utils.reporter import generar_reporte_html
import time

# Configuración del WebDriver
driver = webdriver.Chrome()

# Ir al sitio de la NBA
driver.get("https://www.nba.com/")
driver.maximize_window()
time.sleep(5)


screenshots = ["screenshots/partidos_home.png"]
driver.save_screenshot(screenshots[0])

driver.quit()

generar_reporte_html("Reporte Test Partidos", screenshots, "reports/reporte_partidos.html")
