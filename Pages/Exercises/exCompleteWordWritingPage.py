import time
from locators import Locators
from globalFunctions import *
from exercisesPage import Exercises
from Pages.Exercises.exWritingPage import ExWriting

class ExCompleteWordWriting(ExWriting):

    def __init__(self,driver):
        super().__init__(driver)
        self.isCurrentPageElement = Locators.isCompleteWordWriting   # Overwrite isCurrentPageElement from parent class
        self.isCurrentPageElement2 = ""
        self.name = "completeWordWriting"

        
        # Initialize objects (elements) of this page
        self.writingInput = Locators.completeWordWritingInput           #before press toggle button
        self.writingTextArea = Locators.completeWordWritingTextArea     #after press toggle button


    def solve(self):
        if not self.isToggled():
            self.clickToggleKeyboard() # Toggle to keyboard => Now is a writing exercise
            print("toggle to keyboard")
        super().solve()
    
    def isToggled(self):
        turnOffImplicitWait(self.driver)
        b = len(self.driver.find_elements_by_css_selector(self.writingTextArea))>0
        turnOnImplicitWait(self.driver)
        return b