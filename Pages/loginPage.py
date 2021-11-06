from locators import Locators

class LoginPage():

    def __init__(self,driver):
        self.driver = driver

        #Initialize objects (elements) of this page
        self.buttonStartXpath = Locators.buttonStartXpath
        self.textboxUsernameXpath = Locators.textboxUsernameXpath
        self.textboxPasswordXpath = Locators.textboxPasswordXpath
        self.buttonLoginXpath = Locators.buttonLoginXpath

    def enterUsername(self,username):
        self.driver.find_element_by_xpath(self.textboxUsernameXpath).clear()
        self.driver.find_element_by_xpath(self.textboxUsernameXpath).send_keys(username)

    def enterPassword(self,password):
        self.driver.find_element_by_xpath(self.textboxPasswordXpath).clear()
        self.driver.find_element_by_xpath(self.textboxPasswordXpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.buttonLoginXpath).click()

    def clickStart(self):
        self.driver.find_element_by_xpath(self.buttonStartXpath).click()
