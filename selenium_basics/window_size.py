import time
import unittest

from selenium import webdriver


class WindowSize(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_find_window_size(self):
        self.driver.execute_script("window.location = 'https://learn.letskodeit.com/p/practice';")
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
        height = self.driver.execute_script("return window.innerHeight;")
        width = self.driver.execute_script("return window.innerWidth;")
        print('Height: ' + str(height))
        print('Width: ' + str(width))

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
