from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("http://localhost:81/demophp/src/form2.html")
element = driver.find_element_by_id("type")
select = Select(element)
select.select_by_index(1) #index start from 0
time.sleep(3)
select.select_by_visible_text("Man")
time.sleep(3)
select.select_by_value("W")
time.sleep(3)
driver.quit()
