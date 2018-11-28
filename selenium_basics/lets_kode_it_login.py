import time
import unittest

from selenium import webdriver


class FindByIdName(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test(self):
        self.driver.get('https://learn.letskodeit.com/p/practice')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//div[@id='navbar']//a[@href='/sign_in']").click()
        email_field = self.driver.find_element_by_id('user_email')
        email_field.send_keys('test')
        self.driver.find_element_by_id('user_password').send_keys('test')
        time.sleep(2)
        email_field.clear()
        time.sleep(2)
        email_field.send_keys('test')
        self.driver.find_element_by_xpath("//input[@name='commit']").click()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
