import time
import unittest

from selenium import webdriver
from selenium.webdriver.support.select import Select


class FacebookLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_facebook_login(self):
        self.driver.get('https://www.facebook.com/')
        assert 'facebook' in self.driver.page_source
        self.driver.find_element_by_id('email').send_keys('abc@gmail.com')
        self.driver.find_element_by_id('pass').send_keys('efg')
        # self.driver.find_element_by_id('u_0_n').click()
        self.driver.find_element_by_xpath("//input[@value='Log In']").click()
        time.sleep(1)
        assert 'Log Into Facebook' == self.driver.find_element_by_id('header_block').text
        assert 'The password you’ve entered is incorrect.' in self.driver.page_source
        assert 'Log In' == self.driver.find_element_by_id('loginbutton').text
        assert self.driver.find_element_by_link_text('Recover Your Account').is_displayed()
        time.sleep(1)

    def test_facebook_signup_wrong_data(self):
        self.driver.get('https://www.facebook.com/')
        assert 'facebook' in self.driver.page_source
        self.driver.find_element_by_name('firstname').send_keys('Sri')
        self.driver.find_element_by_name('lastname').send_keys('Rai')
        self.driver.find_element_by_name('reg_email__').send_keys('abc@n')
        self.driver.find_element_by_name('reg_passwd__').send_keys('abc@n')
        select = Select(self.driver.find_element_by_id('month'))
        select.select_by_visible_text('Dec')
        select = Select(self.driver.find_element_by_id('day'))
        select.select_by_value('11')
        select = Select(self.driver.find_element_by_id('year'))
        select.select_by_value('1994')
        self.driver.find_element_by_xpath("//input[@id='u_0_9']").click()
        time.sleep(2)
        self.driver.find_element_by_name('websubmit').click()
        assert 'Please enter a valid email address or mobile number' in self.driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
