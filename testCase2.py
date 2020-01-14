import unittest
from selenium import webdriver

class SearchEngineTest(unittest.TestCase):

    def test_Bing(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://bing.com")
        print("Title is : " + self.driver.title)

    def test_Google(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://google.com/")
        print("Title is : "+ self.driver.title)

if __name__=="__main__":
    unittest.main()
#sort by alphabet Number, A, a