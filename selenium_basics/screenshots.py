import unittest

from selenium import webdriver


class SaveScreenshots(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_save_screenshot(self):
        self.driver.get('https://letskodeit.teachable.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_link_text('Login').click()
        self.driver.find_element_by_id('user_email').send_keys('abc@email.com')
        self.driver.find_element_by_id('user_password').send_keys('test')
        self.driver.find_element_by_name('commit').click()
        destination_file_name = 'D:\\pratima\\tutorials\\QA-testing\\test.png'

        try:
            self.driver.save_screenshot(destination_file_name)
            print('Screenshot saved to directory ' + destination_file_name)

        except NotADirectoryError:
            print('Not a directory issue')

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()