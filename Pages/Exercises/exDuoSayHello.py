from locators import Locators
from globalFunctions import *
from exercisesPage import Exercises
import time

class ExDuoSayHello(Exercises):

    def __init__(self,driver):
        super().__init__(driver)
        self.isCurrentPageElement = ""   # Overwrite isCurrentPageElement from parent class
        self.isFinalPage = Locators.isFinalPage
        self.name = "duoSayHello"
    
    def solve(self):
        time.sleep(1)
        self.clickButtonCheck()    
        
    def isCurrentPage(self):      
        # ExDuoSayHello overwite parent's function  
        print("\n")
        print("isCurrentPage in duoSayHello")
        print("\n")
        turnOffImplicitWait(self.driver)
        header = self.driver.find_elements_by_css_selector(self.header)
        buttonCheck = self.driver.find_elements_by_css_selector(self.buttonCheck)
        isFinalPage = self.driver.find_elements_by_css_selector(self.isFinalPage)
        turnOnImplicitWait(self.driver)
        print("(len(buttonCheck) > 0) = " + str(len(buttonCheck)))
        print("(len(header) > 0) = " + str(len(header)))

        return (len(buttonCheck) > 0) and (len(header) <= 0) and (len(isFinalPage)<=0)