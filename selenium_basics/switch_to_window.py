import time
import unittest

from selenium import webdriver


class SwitchWindow(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_to_switch_window(self):
        self.driver.get('https://learn.letskodeit.com/p/practice')
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)

        # Find parent handle --> Main window
        parent_handle = self.driver.current_window_handle
        print("Parent handle: " + parent_handle)

        # Find open window button and click it
        self.driver.find_element_by_id('openwindow').click()
        time.sleep(2)

        # Find all the window handles, there should be two handles after clicking the open window button
        handles = self.driver.window_handles

        # Switch to window and search course
        for handle in handles:
            print(handle)

            if handle not in parent_handle:
                self.driver.switch_to.window(handle)
                print("Switched to window: " + handle)

                search_box = self.driver.find_element_by_id("search-courses")
                search_box.send_keys('Python')
                time.sleep(2)
                break

        # Switch back to parent handle
        self.driver.switch_to.window(parent_handle)
        self.driver.find_element_by_id('name').send_keys('Test successful')
        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
