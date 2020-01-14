from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.python.org")
driver.get("https://www.perl.org")
driver.forward()
driver.back()
