import unittest

from selenium import webdriver


class FindByIdName(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test(self):
        self.driver.get('https://learn.letskodeit.com/p/practice')
        element_by_id = self.driver.find_element_by_id('name')

        if element_by_id is not None:
            print('We found an element by ID')

        element_by_name = self.driver.find_element_by_name('show-hide')

        if element_by_name is not None:
            print('We found an element by name')

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
