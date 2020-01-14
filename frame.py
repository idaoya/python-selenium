from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://localhost:81/norsk/src/")

fr=driver.find_element_by_tag_name('frame_a')
driver.switch_to.frame(fr)