from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("http://localhost:81/tm/src/web/dictionary/")
element = driver.find_element_by_name("en")
is_check = element.is_selected()

print(is_check)
driver.close()