from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("http://localhost:8181/JavaServerFaces/")

# Now set the cookie. This one's valid for the entire domain
cookie = {'name':'foo', 'value':'bar'}
driver.add_cookie(cookie)

driver.get_cookies()

print(len(cookie))
print(cookie)

time.sleep(5)
driver.close()