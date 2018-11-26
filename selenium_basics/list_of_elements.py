import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class ListOfElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test(self):
        self.driver.get('https://learn.letskodeit.com/p/practice')
        element_list_by_class_name = self.driver.find_elements_by_class_name('inputs')
        length1 = len(element_list_by_class_name)

        if element_list_by_class_name is not None:
            print('The size of the list is: ' + str(length1))

        element_list_by_tag_name = self.driver.find_elements(By.TAG_NAME, 'h1')
        length2 = len(element_list_by_tag_name)

        if element_list_by_tag_name is not None:
            print('The size of the list is: ' + str(length2))

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
