import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_python_org_search_with_invalid_word(self):
        self.driver.get("http://www.python.org")
        assert "Welcome to Python.org" == self.driver.title
        time.sleep(2)

        search_bar = self.driver.find_element_by_id('id-search-field')
        search_bar.clear()
        search_bar.send_keys('Pratima')
        time.sleep(2)
        search_bar.send_keys(Keys.RETURN)
        assert 'No results found.' in self.driver.page_source
        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
