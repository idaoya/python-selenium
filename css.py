from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://localhost:81/demophp/src/form2.html")

#<button type="submit" name="login" class="big button">Log in</button>&nbsp;
#<button type="submit" name="cancel" class="big button">Cancel</button>

#Show the last button
element=driver.find_element_by_css_selector(".big + .button")
time.sleep(4)
element.click()

driver.quit