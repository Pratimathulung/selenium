import time
import unittest

from selenium import webdriver
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium_basics.handy_wrappers import HandyWrappers


class DynamicXpathFormat(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_with_dynamic_xpath(self):
        self.driver.get('https://learn.letskodeit.com/p/practice')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        hw = HandyWrappers(self.driver)
        hw.getElement("//div[@id='navbar']//a[@href='/sign_in']", 'xpath').click()
        hw.getElement('user_email', 'id').send_keys('test@email.com')
        hw.getElement('user_password', 'id').send_keys('abcabc')
        hw.getElement('commit', 'name').click()

        search_bar = hw.getElement('query', 'name')
        search_bar.clear()
        search_bar.send_keys('JavaScript')
        search_bar.send_keys(Keys.RETURN)

        course = "//div[contains(@class,'course-listing-title')and contains(text(),'{0}')]"
        course_locator = course.format('JavaScript for beginners')

        course_element = hw.getElement(course_locator, 'xpath')
        course_element.click()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()