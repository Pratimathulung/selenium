import time
import unittest

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ExplicitWaitDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_using_explicit_wait(self):
        self.driver.get('https://www.expedia.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(.5)
        self.driver.find_element_by_id('tab-flight-tab-hp').click()
        self.driver.find_element_by_xpath("//input[@id='flight-origin-hp-flight']").send_keys('Portland')
        self.driver.find_element_by_xpath("//input[@id='flight-destination-hp-flight']").send_keys('SFO')
        departure_date = self.driver.find_element_by_id('flight-departing-hp-flight')
        departure_date.click()
        departure_date.send_keys("12/24/2018")
        return_date = self.driver.find_element_by_xpath("//input[@id='flight-returning-hp-flight']")
        return_date.clear()
        return_date.click()
        return_date.send_keys("12/28/2018")
        time.sleep(5)
        self.driver.find_element_by_xpath("/html//form[@id='gcw-flights-form-hp-flight']//button[@type='submit']").click()

        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.ID, 'stopFilter_stops-0')))
        element.click()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
