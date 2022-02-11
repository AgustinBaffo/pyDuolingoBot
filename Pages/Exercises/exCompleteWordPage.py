import time
from locators import Locators
from globalFunctions import *
from exercisesPage import Exercises

class ExCompleteWord(Exercises):

    def __init__(self,driver):
        super().__init__(driver)
        self.isCurrentPageElement = Locators.isCompleteWord   # Overwrite isCurrentPageElement from parent class
        self.name = "completeWord"

        # Initialize objects (elements) of this page
        self.req = Locators.completeWordReq
        self.completeWordOptions = Locators.completeWordOptions
        self.completeWordOptionsInput = Locators.completeWordOptionsInput
        self.completeWordOptionsText = Locators.completeWordOptionsText
        
    def clickByIndex(self,i):        
        self.optionElement[i].click()

    def clickByString(self,w):
        self.optionElement[self.optionList.index(w)].click()
    
    def solveKnown(self,s):
        print("known request")
        self.clickByString(s)
        print("clicked")

    def solveUnknown(self):
        print("unknown request")
        self.clickByIndex(0)        
        print("word 1 selected")
        time.sleep(1)

    def solve(self):
        req = self.getReq()   # returns "bla bla ___ bla"
        print("request = "+req)
        options = self.getOptions()
        print(options)

        isknow = False
        needLearn = False

        for s in options:
            testResult = req.replace("___",s)
            print("testResult = " + testResult)
            testTr = translate(testResult,getTranslations()).lower()            
            print("testTr = " + testTr)
            if testTr != "":
                isknow = True
                self.solveKnown(s)
                continue
        if not isknow:
            self.solveUnknown()

        print("click button check")
        self.clickButtonCheck()
        
        # Check if correct
        if(self.isCorrect()):
            print("*-*-*-*-*-*-* CORRECT *-*-*-*-*-*")            
            if(needLearn):
                print("############################")
                print("check if it works")
                print("luckly got it right")
                print("############################")
                testResult = req.remplace("___",options[0])
                print("testResult = " + testResult)
                print("need lern a = " + testResult + ", b = " + testTr)
                learn(testResult,testTr)
        else:
            print("*-*-*-*-*-*-* INCORRECT *-*-*-*-*-*")
            answ = self.getCorrectAnswer()
            print("need lern a = " + answ + ", b = " + req)
            input() #check it
            learn(answ,req)

        self.clickButtonCheck()

    def getReq(self):        
        req = self.driver.find_element_by_css_selector(self.req)
        return cleanStringSpecialCharacters(str(req.get_attribute('data-prompt')))

    def getOptions(self):
        self.optionElement = self.driver.find_elements_by_css_selector(self.completeWordOptionsText)
        print("options elements found")
        self.optionList = []
        for w in self.optionElement:
            print(cleanStringSpecialCharacters(str(w.get_attribute("innerHTML"))))
            self.optionList.append(cleanStringSpecialCharacters(str(w.get_attribute("innerHTML"))))
        return self.optionList