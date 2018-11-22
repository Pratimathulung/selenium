import unittest

from selenium import webdriver


class FindByXpathCss(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test(self):
        self.driver.get('https://learn.letskodeit.com/p/practice')
        element_by_xpath = self.driver.find_element_by_xpath("//input[@id = 'name']")

        if element_by_xpath is not None:
            print('We found an element by Xpath')

        element_by_Css = self.driver.find_element_by_css_selector('#displayed-text')
        if element_by_Css is not None:
            print('We found an element by Css')

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
