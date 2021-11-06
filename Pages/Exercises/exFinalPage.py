from locators import Locators
from globalFunctions import *
from exercisesPage import Exercises
import time

class ExFinalPage(Exercises):

    def __init__(self,driver):
        super().__init__(driver)
        self.isCurrentPageElement = Locators.isFinalPage   # Overwrite isCurrentPageElement from parent class
        self.name = "final"

        # Initialize objects (elements) of this page
        self.buttonNoThanksToPlus = Locators.buttonNoThanksToPlus
    
    def solve(self):
        print("solving final screen")    
        turnOffImplicitWait(self.driver)
        buttonCheckExist = len(self.driver.find_elements_by_css_selector(self.buttonCheck)) > 0
        buttonNoThanksToPlusExist = len(self.driver.find_elements_by_css_selector(self.buttonNoThanksToPlus)) > 0 
        while buttonCheckExist:
            if buttonNoThanksToPlusExist:
                self.clickButtonNoThanksToPlus()
                break                
            self.clickButtonCheck()
            time.sleep(2)
            buttonCheckExist = len(self.driver.find_elements_by_css_selector(self.buttonCheck)) > 0
            buttonNoThanksToPlusExist = len(self.driver.find_elements_by_css_selector(self.buttonNoThanksToPlus)) > 0  
            print("New Button = " + str(buttonCheckExist) + ". Amount = " + str(len(self.driver.find_elements_by_css_selector(self.buttonCheck))))
            print("ButtonNoThanksToPlus = " + str(buttonNoThanksToPlusExist) + ". Amount = " + str(len(self.driver.find_elements_by_css_selector(self.buttonNoThanksToPlus))))
        print("\n*-*-* final screen solved ! *-*-*\n")      
        turnOnImplicitWait(self.driver)

    def clickButtonNoThanksToPlus(self):
        self.driver.find_element_by_css_selector(self.buttonNoThanksToPlus).click()
            