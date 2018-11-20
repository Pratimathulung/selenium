import unittest

from selenium import webdriver


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_python_org_search_with_invalid_word(self):
        self.driver.get("http://www.python.org")
        assert "Welcome to Python.org" == self.driver.title

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
