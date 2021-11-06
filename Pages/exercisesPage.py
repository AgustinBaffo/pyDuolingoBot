from Libraries.globalFunctions import *
from locators import Locators

class Exercises:
    # This class contains common elements and functions of all exercises

    def __init__(self,driver):
        self.driver = driver
            
        self.buttonQuit = Locators.buttonQuit
        self.header = Locators.header
        self.buttonSkip = Locators.buttonSkip
        self.buttonCheck = Locators.buttonCheck
        
        self.answStatus = Locators.answStatus
        self.isIncorrectAnsw = Locators.isIncorrectAnsw
        self.isCorrectAnsw = Locators.isCorrectAnsw
        self.correctAnsw = Locators.correctAnsw
        self.toggleKeyboard = Locators.toggleKeyboard

        self.isCurrentPageElement = ""
        self.isCurrentPageElement2 = ""
        
    def getCorrectAnswer(self):
        answElements = self.driver.find_element_by_css_selector(self.correctAnsw)
        return cleanStringSpecialCharacters(str(answElements.get_attribute("innerHTML")))

    def isCorrect(self):
        setImplicitWait(self.driver,True,3)
        answElements = self.driver.find_elements_by_css_selector(self.isCorrectAnsw)
        setImplicitWait(self.driver,True)
        return len(answElements) > 0
        
    def clickButtonCheck(self):
        self.driver.find_element_by_css_selector(self.buttonCheck).click()

    def clickButtonSkip(self):
        self.driver.find_element_by_css_selector(self.buttonSkip).click()

    def clickButtonQuit(self):
        self.driver.find_element_by_css_selector(self.buttonQuit).click()
    
    def isCurrentPage(self):        
        print("\n")
        print("isCurrentPage testing with locator: " + str(self.isCurrentPageElement))
        turnOffImplicitWait(self.driver)
        searchElement = self.driver.find_elements_by_css_selector(self.isCurrentPageElement)
        if(self.isCurrentPageElement2 != ""):
            searchElement2 = self.driver.find_elements_by_css_selector(self.isCurrentPageElement2)
        else:
            searchElement2 = searchElement
        turnOnImplicitWait(self.driver)
        return len(searchElement) > 0 and len(searchElement2)

    def clickToggleKeyboard(self):
        self.driver.find_element_by_css_selector(self.toggleKeyboard).click()