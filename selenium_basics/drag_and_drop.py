import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains


class DragAndDrop(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_to_drag_and_drop(self):
        self.driver.get('https://jqueryui.com/droppable/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
        self.driver.switch_to.frame(0)

        fromElement = self.driver.find_element_by_id('draggable')
        toElement = self.driver.find_element_by_id('droppable')
        time.sleep(2)

        try:
            actions = ActionChains(self.driver)
            # actions.drag_and_drop(fromElement, toElement).perform()
            actions.click_and_hold(fromElement).move_to_element(toElement).release().perform()
            print('Drag and Drop element successful')
            time.sleep(2)

        except:
            print('Drag and Drop failed on element')

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
