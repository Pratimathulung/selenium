from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_basics.framework_structures.pages.home.login_page import LoginPage
import unittest


class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        baseURL = "https://letskodeit.teachable.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        lp = LoginPage(driver)
        lp.login("test@email.com", "abcabc")

        userIcon = driver.find_element(By.XPATH,
                                       "/html//div[@id='navbar']//ul[@class='nav navbar-nav navbar-right']/li[@class='dropdown']/a/img[@alt='test@email.com']")
        if userIcon is not None:
            print("Login Successful")
        else:
            print("Login Failed")
