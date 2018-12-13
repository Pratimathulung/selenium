from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_basics.framework_structures.pages.home.login_page import LoginPage
import unittest

class LoginTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_validLogin(self):
        baseURL = "https://letskodeit.teachable.com/"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get(baseURL)

        lp = LoginPage(self.driver)
        lp.login("test@email.com", "abcabc")

        userIcon = self.driver.find_element(By.XPATH,
                                       "/html//div[@id='navbar']//ul[@class='nav navbar-nav navbar-right']/li[@class='dropdown']/a/img[@alt='test@email.com']")
        if userIcon is not None:
            print("Login Successful")
        else:
            print("Login Failed")

    def tearDown(self):
        self.driver.close()

