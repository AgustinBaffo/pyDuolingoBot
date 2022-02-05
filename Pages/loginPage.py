from locators import Locators

class LoginPage():

    def __init__(self,driver):
        self.driver = driver

        #Initialize objects (elements) of this page
        self.buttonStartCS = Locators.buttonStartCS
        self.textboxUsernameCS = Locators.textboxUsernameCS
        self.textboxPasswordCS = Locators.textboxPasswordCS
        self.buttonLoginCS = Locators.buttonLoginCS

    def enterUsername(self,username):
        self.driver.find_element_by_css_selector(self.textboxUsernameCS).clear()
        self.driver.find_element_by_css_selector(self.textboxUsernameCS).send_keys(username)

    def enterPassword(self,password):
        self.driver.find_element_by_css_selector(self.textboxPasswordCS).clear()
        self.driver.find_element_by_css_selector(self.textboxPasswordCS).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_css_selector(self.buttonLoginCS).click()

    def clickStart(self):
        self.driver.find_element_by_css_selector(self.buttonStartCS).click()
