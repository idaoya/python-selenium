from selenium import webdriver
from selenium.webdriver.common.keys import Keys

dr1 = webdriver.Chrome()
dr2 = webdriver.Firefox()

dr1.get("https://python.org")
python_title = dr1.title
dr2.get(python_title)
dr2.get("https://perl.org")