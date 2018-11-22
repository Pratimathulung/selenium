import unittest

from selenium import webdriver


class FindByLinkTxt(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test(self):
        self.driver.get('https://learn.letskodeit.com/p/practice')
        element_by_link_txt = self.driver.find_element_by_link_text('Login')

        if element_by_link_txt is not None:
            print('We found an element by LinkTxt')

        element_by_partial_linktxt = self.driver.find_element_by_partial_link_text('Prac')

        if element_by_partial_linktxt is not None:
            print('We found an element by Partial Link text')

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
