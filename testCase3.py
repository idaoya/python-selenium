import unittest

class AppTesting(unittest.TestCase):

    @unittest.skip("showing class skipping")
    def test_search(self):
        print("search")

    def test_advanceSearch(self):
        print("advanceSearch")

if __name__ =="__main__":
    unittest.main()