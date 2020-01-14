from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://localhost:81/demophp/src/form2.html")
try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "noID"))
    )
finally:
    driver.quit()