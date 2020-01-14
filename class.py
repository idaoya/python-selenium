from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://localhost:81/demophp/src/form.html")

#< button type = "submit" name = "cancel" class ="big button" > Cancel < / button >

element=driver.find_element_by_css_selector(".big.button[name='cancel'")
print(element)