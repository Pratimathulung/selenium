import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class MouseHoveringAction(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_to_hover_mouse(self):
        self.driver.get('https://learn.letskodeit.com/p/practice')
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
        self.driver.execute_script("window.scrollBy(0,800);")
        time.sleep(2)
        element = self.driver.find_element_by_id('mousehover')

        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            print("Mouse hovered on element")
            time.sleep(2)
            top_link = self.driver.find_element_by_xpath("//div[@class='mouse-hover-content']//a[text()='Top']")
            actions.move_to_element(top_link).click().perform()
            print("Item clicked")

        except:
            print("Mouse hover failed on element")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
