from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("http://localhost:81/demophp/src/")
assert "Python" in driver.title

elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("demo")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

time.sleep(5)
driver.close()