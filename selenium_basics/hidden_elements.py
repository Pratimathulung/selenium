import time
import unittest

from selenium import webdriver


class HiddenElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_lets_kode_it(self):
        self.driver.get('https://learn.letskodeit.com/p/practice')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        # Find the state of the text box
        text_box_element = self.driver.find_element_by_id('displayed-text')
        text_box_element_state = text_box_element.is_displayed()
        self.assertTrue(text_box_element_state, msg='Text box should be displayed')
        time.sleep(2)

        # Click the hide button
        self.driver.find_element_by_id('hide-textbox').click()
        # Find the state of the text box
        text_box_element_state = text_box_element.is_displayed()
        self.assertFalse(text_box_element_state, msg='Text box should be hidden')

        # Click the show button
        self.driver.find_element_by_id('show-textbox').click()
        # Find the state of the text box
        text_box_element_state = text_box_element.is_displayed()
        self.assertTrue(text_box_element_state, msg='Text box should be displayed.')
        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
