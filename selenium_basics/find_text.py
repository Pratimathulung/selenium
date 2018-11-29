import time
import unittest

from selenium import webdriver


class FindText(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_find_text(self):
        self.driver.get('https://learn.letskodeit.com/p/practice')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        open_tab_window = self.driver.find_element_by_id('opentab')
        element_text = open_tab_window.text
        self.assertTrue(element_text, msg='Text on element is Open Tab')
        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

