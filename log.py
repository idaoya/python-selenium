from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logging as logg

logg.basicConfig(level=logg.INFO)
test_data = "Hello world"
logg.info("Line 3")
logg.debug("Line 4")
logg.warning("Line 5")
logg.error("Line 6")
assert test_data == "Hello world", "Wrong test data"
logg.info("Line 7")