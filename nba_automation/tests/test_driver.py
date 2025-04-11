from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
# NO HEADLESS → esto es porque queremos ver que se abra, lo tome como prueba xd
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com")
input("Presiona ENTER para cerrar...")
driver.quit()
