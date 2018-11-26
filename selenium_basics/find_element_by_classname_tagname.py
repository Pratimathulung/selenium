import unittest

from selenium import webdriver


class FindByIdClassNameTagName(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test(self):
        self.driver.get('https://learn.letskodeit.com/p/practice')
        element_by_class_name = self.driver.find_element_by_class_name('displayed-class')

        if element_by_class_name is not None:
            print('We found an element by class name')

        element_by_tag_name = self.driver.find_element_by_tag_name('a')

        if element_by_tag_name is not None:
            print('We found an element by tag name')

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
