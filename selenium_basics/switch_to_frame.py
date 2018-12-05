import time
import unittest

from selenium import webdriver


class SwitchFrame(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_to_switch_frame(self):
        self.driver.get('https://learn.letskodeit.com/p/practice')
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
        self.driver.execute_script("window.scrollBy(0,2000);")

        # Find parent handle --> Main window
        parent_handle = self.driver.current_window_handle
        print("Parent handle: " + parent_handle)

        # Switch to frame using ID
        # self.driver.switch_to.frame('courses-iframe')

        # Switch to frame using Name
        # self.driver.switch_to.frame('iframe-name')

        # Switch to frame using Number
        self.driver.switch_to.frame(0)

        time.sleep(2)

        # Search course
        search_box = self.driver.find_element_by_id("search-courses")
        search_box.send_keys('Python')
        time.sleep(2)

        # Switch back to parent frame
        self.driver.switch_to.default_content()
        self.driver.execute_script("window.scrollBy(0,-2000);")
        time.sleep(2)
        self.driver.find_element_by_id('name').send_keys('Test successful')
        time.sleep(2)






    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
