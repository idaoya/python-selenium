from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://localhost:81/demophp/src/weather.xml")

element=driver.find_element_by_xpath("//temperature[@city=New York]/@UoM")
print(element)
driver.quit