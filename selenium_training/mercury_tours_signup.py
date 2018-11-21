import unittest

from selenium import webdriver
from selenium.webdriver.support.select import Select


class MercuryTourSignUp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_signup(self):
        self.driver.get('http://newtours.demoaut.com/')
        self.driver.find_element_by_link_text('REGISTER').click()
        assert 'Contact' in self.driver.page_source
        self.driver.find_element_by_name('firstName').send_keys('Pratima')
        self.driver.find_element_by_name('lastName').send_keys('Rai')
        self.driver.find_element_by_name('phone').send_keys('213647')
        self.driver.find_element_by_name('userName').send_keys('abc@mail.com')
        self.driver.find_element_by_name('address1').send_keys('beaverton')
        self.driver.find_element_by_name('email').send_keys('pratima')
        select = Select(self.driver.find_element_by_name('country'))
        select.select_by_visible_text('NEPAL')

        self.driver.find_element_by_name('register').click()
        assert 'Thank you for registering.' in self.driver.page_source
        assert 'Note: Your user name is pratima.' in self.driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
