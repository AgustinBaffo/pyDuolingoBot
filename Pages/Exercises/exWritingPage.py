import time
from locators import Locators
from globalFunctions import *
from exercisesPage import Exercises

class ExWriting(Exercises):

    def __init__(self,driver):
        super().__init__(driver)
        self.isCurrentPageElement = Locators.isWriting1   # Overwrite isCurrentPageElement from parent class
        self.isCurrentPageElement2 = Locators.isWriting2
        self.name = "writing"

        # Initialize objects (elements) of this page
        self.req = Locators.writingReq
        self.textArea = Locators.writingTextArea
        
    def solveKnown(self,trReq):
        print("known request")
        time.sleep(1)
        self.driver.find_element_by_css_selector(self.textArea).send_keys(str(trReq))

    def solveUnknown(self):
        print("unknown request")
        time.sleep(1)
        self.driver.find_element_by_css_selector(self.textArea).send_keys("I don't know yet :(")
    

    def solve(self):
        req = self.getReq()
        print("request = "+req)
        trReq = translate(req,getTranslations()).lower()
        print("trReq = "+trReq)

        # Validate if translation exist
        if trReq != "":
            self.solveKnown(trReq)
        else:
            self.solveUnknown()

        print("click button check")    
        time.sleep(1)
        self.clickButtonCheck()
        
        # Check if correct
        if(self.isCorrect()):
            print("*-*-*-*-*-*-* CORRECT *-*-*-*-*-*")
        else:
            print("*-*-*-*-*-*-* INCORRECT *-*-*-*-*-*")
            answ = self.getCorrectAnswer()
            print("need lern a = " + answ + ", b = " + req)
            learn(answ,req)

        self.clickButtonCheck()

    def getWordsFromReq(self):
        print("getWordsFromReq called")
        self.wordReqElement = self.driver.find_elements_by_css_selector(self.req)
        print("wordReqElement found")
        req = []
        for w in self.wordReqElement:
            print((str(w.get_attribute("innerHTML")).lower()))
            req.append(str(w.get_attribute("innerHTML")).lower())
        print(req)
        req = cleanListSpecialCharacters(req)        
        print("getWordsFromReq end")
        return req

    def getReq(self):
        return cleanStringSpecialCharacters(str(' '.join(self.getWordsFromReq())))
