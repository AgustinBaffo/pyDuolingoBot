import time
from locators import Locators
from globalFunctions import *
from exercisesPage import Exercises

class ExSelectSentence(Exercises):

    def __init__(self,driver):
        super().__init__(driver)
        self.isCurrentPageElement = Locators.isSelectSentence   # Overwrite isCurrentPageElement from parent class
        self.name = "selectSentence"

        # Initialize objects (elements) of this page
        self.selectReq = Locators.selectSentenceReq
        self.selectSentenceOptions = Locators.selectSentenceOptions
        self.selectSentenceOptionsInput = Locators.selectSentenceOptionsInput
        self.selectSentenceOptionsText = Locators.selectSentenceOptionsText

    def clickByIndex(self,i):   
        self.optionElement[i].click()

    def clickByString(self,w):
        print("clickByString: "+ w)
        print("list = ")
        print(self.optionList)

        self.optionElement[self.optionList.index(w)].click()
    
    def solveKnown(self,trReq):
        print("known request")
        self.clickByString(trReq)

    def solveUnknown(self):
        print("unknown request")
        self.clickByIndex(0)        
        print("option 1 selected")
        time.sleep(1)
    

    def solve(self):
        req = self.getReq()
        print("request = "+req)
        options = self.getSentences()
        print(options)

        trReq = translate(req,getTranslations()).lower()
        print("trReq = "+trReq)
        
        needLearn = False

        # Validate if translation exist
        if trReq != "":
            self.solveKnown(trReq)
        else:
            needLearn = True
            self.solveUnknown()
                    
        self.clickButtonCheck()
        
        # Check if correct
        if(self.isCorrect()):
            print("*-*-*-*-*-*-* CORRECT *-*-*-*-*-*")            
            if(needLearn):
                print("############################")
                print("check if it works")
                print("luckly got it right")
                print("############################")
                answ = cleanStringSpecialCharacters(str(self.optionList[0]))
                print("need lern a = " + trReq + ", b = " + req)
                learn(answ,req)
        else:
            print("*-*-*-*-*-*-* INCORRECT *-*-*-*-*-*")
            answ = self.getCorrectAnswer()
            print("need lern a = " + answ + ", b = " + req)
            learn(answ,req)

        self.clickButtonCheck()

    def getReq(self):
        reqElement = self.driver.find_element_by_css_selector(self.selectReq)
        return cleanStringSpecialCharacters(str(reqElement.get_attribute("innerHTML")))

    def getSentences(self):
        self.optionElement = self.driver.find_elements_by_css_selector(self.selectSentenceOptionsText)
        self.optionList = []
        for s in self.optionElement:
            print(cleanStringSpecialCharacters(str(s.get_attribute("innerHTML"))))
            self.optionList.append(cleanStringSpecialCharacters(str(s.get_attribute("innerHTML"))))
        return self.optionList