from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(5) #seconds
driver.get("http://localhost:81/demophp/src/form2.html")
myDynamicElement = driver.find_element_by_id("noID")