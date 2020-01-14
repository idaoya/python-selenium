from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

def click_by_xpath(driver, path):
 try:
    element.wait(driver,5).until
    EC.presence_of_element_located(By.xpath, path)
    element.click()
 except TimeoutException:
    element=None
 return element