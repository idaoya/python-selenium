from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://localhost:81/demophp/src/")
driver.maximize_window()
driver.save_screenshot("D://pythonproject//screenshot/test1.png")
driver.get_screenshot_as_file("D://pythonproject//screenshot/test2.jpg")
driver.quit()