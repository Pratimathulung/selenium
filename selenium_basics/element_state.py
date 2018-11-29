import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ElementState(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_is_enabled(self):
        self.driver.get('https://www.google.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

        element = self.driver.find_element_by_name("q")
        element_state = element.is_enabled()
        assert element_state is True

        if element_state is True:
            element.send_keys('Coding is fun')
            element.send_keys(Keys.RETURN)
            time.sleep(2)
            assert self.driver.find_element_by_id('resultStats').is_displayed()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

