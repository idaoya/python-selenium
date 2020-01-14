from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#driver = webdriver.Chrome(executable_path="D:\pythonproject\chromedriver.exe")
driver = webdriver.Chrome()
driver.get("http://localhost:81/demophp/src/alert.html")
b = driver.find_element_by_xpath("/html/body/button")
b.click()

alert=driver.switch_to.alert
msg=alert.text
assert "Press a button!" in msg
print(msg)
time.sleep(4)
#alert.accept()
alert.dismiss()

msg_display =driver.find_element_by_xpath("//*[@id='demo']").text
print(msg_display)

time.sleep(3)
driver.quit()