from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    #locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"

    def getLoginLink(self):
        return self.driver.find_element(By.LINK_TEXT, self._login_link)

    def getEmailField(self):
        return self.driver.find_element(By.ID, self._email_field)

    def getPasswordField(self):
        return self.driver.find_element(By.ID, self._password_field)

    def getLoginButton(self):
        return self.driver.find_element(By.NAME, self._login_button)

    def clickLoginLink(self):
        self.getLoginLink().click()


    def enterEmail(self, email):
        self.getEmailField().send_keys(email)

    def enterPassword(self, password):
        self.getPasswordField().send_keys(password)

    def clickLoginButton(self):
        self.getLoginButton().click()

    def login(self, email, password):
        self.clickLoginButton()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

        loginLink = self.driver.find_element(By.LINK_TEXT, "Login")
        loginLink.click()

        emailField = self.driver.find_element(By.ID, "user_email")
        emailField.send_keys(username)

        passwordField = self.driver.find_element(By.ID, "user_password")
        passwordField.send_keys(password)

        loginButton = self.driver.find_element(By.NAME, "commit")
        loginButton.click()