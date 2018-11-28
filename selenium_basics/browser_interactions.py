import unittest

from selenium import webdriver


class BrowserInteractions(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test(self):
        baseUrl = 'https://learn.letskodeit.com/p/practice'

        # Window Maximize
        self.driver.maximize_window()
        # Open the Url
        self.driver.get(baseUrl)
        # Get Title
        title = self.driver.title
        print('The title of the web page is: ' + title)
        # Get current Url
        currentUrl = self.driver.current_url
        print('Current Url of the webpage is: ' + currentUrl)
        # Browser refresh
        self.driver.refresh()
        print('Browser refresed for first time')
        self.driver.get(self.driver.current_url)
        print('Browser refreshed 2nd time')
        # Browser forward
        self.driver.forward()
        print('Go one step forward in browser history')
        # Get page source
        pageSource = self.driver.page_source
        # browser close/ quit
        # self.driver.close()
        # self.driver.quit()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
