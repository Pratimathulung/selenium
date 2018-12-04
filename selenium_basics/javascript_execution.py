import time
import unittest

from selenium import webdriver


class JavaScriptExecution(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test(self):
        # self.driver.get('https://learn.letskodeit.com/p/practice')
        self.driver.execute_script("window.location = 'https://learn.letskodeit.com/p/practice';")
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
        # element = self.driver.find_element_by_id('name')
        element = self.driver.execute_script("return document.getElementById('name')")
        element.send_keys('Test')
        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
