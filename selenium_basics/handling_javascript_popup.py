import time
import unittest

from selenium import webdriver


class HandlingJavaScriptPopup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_to_switch_to_alert(self):
        self.driver.get('https://learn.letskodeit.com/p/practice')
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)

        self.driver.find_element_by_id('name').send_keys('Pratima')
        self.driver.find_element_by_id('alertbtn').click()
        time.sleep(2)
        alert1 = self.driver.switch_to.alert
        alert1.accept()
        time.sleep(2)

        self.driver.find_element_by_id('name').send_keys('Pratima')
        self.driver.find_element_by_id('confirmbtn').click()
        time.sleep(2)
        alert2 = self.driver.switch_to.alert
        alert2.dismiss()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
