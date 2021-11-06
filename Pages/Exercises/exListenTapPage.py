from locators import Locators
from globalFunctions import *
from exercisesPage import Exercises
import time

class ExListenTap(Exercises):

    def __init__(self,driver):
        super().__init__(driver)
        self.isCurrentPageElement = Locators.isListenTap   # Overwrite isCurrentPageElement from parent class
        self.name = "listenTap"

        # Initialize objects (elements) of this page
        self.buttonSkip = Locators.buttonSkip
    
    def solve(self):       
        self.clickButtonSkip()
        time.sleep(1)
        self.clickButtonCheck()