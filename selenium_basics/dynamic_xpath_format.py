import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# from selenium_basics.handy_wrappers import HandyWrappers


class DynamicXpathFormat(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_with_dynamic_xpath(self):
        self.driver.get('https://learn.letskodeit.com/p/practice')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//div[@id='navbar']//a[@href='/sign_in']").click()
        self.driver.find_element_by_id('user_email').send_keys('test@email.com')
        self.driver.find_element_by_id('user_password').send_keys('abcabc')
        self.driver.find_element_by_name('commit').click()

        search_bar = self.driver.find_element_by_name('query')
        search_bar.clear()
        search_bar.send_keys('JavaScript')
        search_bar.send_keys(Keys.RETURN)

        course = "//div[contains(@class,'course-listing-title')and contains(text(),'{0}')]"
        course_locator = course.format('JavaScript for beginners')

        course_element = self.driver.find_element(By.XPATH, course_locator)
        course_element.click()
        time.sleep(5)


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()