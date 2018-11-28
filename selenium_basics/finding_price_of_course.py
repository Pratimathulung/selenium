import unittest

from selenium import webdriver


class FindByXpathAndParentSibling(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_using_parent_sibling(self):
        self.driver.get('https://learn.letskodeit.com/p/practice')
        assert self.driver.find_element_by_xpath("//h1[text()='Practice Page']").is_displayed()
        self.driver.find_element_by_xpath(
            "//table[@id='product']//td[text()='Python Programming Language']//following-sibling::td")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
