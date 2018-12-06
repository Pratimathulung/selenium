import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains


class Sliders(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_sliding(self):
        self.driver.get('https://jqueryui.com/slider/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
        self.driver.switch_to.frame(0)

        element = self.driver.find_element_by_xpath("//div[@id='slider']//span")
        time.sleep(2)

        try:
            actions = ActionChains(self.driver)
            actions.drag_and_drop_by_offset(element, 100, 0).perform()
            time.sleep(2)
            print('Sliding element successful')
            time.sleep(2)

        except:
            print('Sliding failed on element')

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
