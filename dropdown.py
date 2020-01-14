from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()

driver.get("http://localhost:81/tm/src/web/dictionary/")
dropdown = driver.find_element_by_name("type")
element = dropdown.find_element_by_xpath("//*[@id='wrapper']/div/div/div[1]/section/form/table/tbody/tr[4]/td[2]/div/select/option[4]")
element.click()

time.sleep(5)
driver.quit()
