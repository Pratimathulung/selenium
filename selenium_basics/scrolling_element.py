import time
import unittest

from selenium import webdriver


class ScrollingElement(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_scroll_element(self):
        self.driver.execute_script("window.location = 'https://learn.letskodeit.com/p/practice';")
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)

        # Scroll Down
        self.driver.execute_script("window.scrollBy(0,2000);")
        time.sleep(2)

        # Scroll Up
        self.driver.execute_script("window.scrollBy(0,-2000);")
        time.sleep(2)

        # Scroll element into view
        element = self.driver.find_element_by_id('mousehover')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0,-150)")
        time.sleep(3)

        # Native way to scroll element into view
        self.driver.execute_script("window.scrollBy(0,-2000);")
        location = element.location_once_scrolled_into_view
        print("Location: " + str(location))

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
