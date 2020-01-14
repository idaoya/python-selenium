from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://localhost:81/frilanse/")

element=driver.find_element_by_id("logginn")
element_text=element.text
print(element_text)