import time
from locators import Locators
from globalFunctions import *
from exercisesPage import Exercises

class ExSelectWordsPage(Exercises):

    def __init__(self,driver):
        super().__init__(driver)
        self.isCurrentPageElement = Locators.isSelectWords1   # Overwrite isCurrentPageElement from parent class
        self.isCurrentPageElement2 = Locators.isSelectWords2
        self.name = "selectWords"

        # Initialize objects (elements) of this page
        self.req = Locators.selectWordsReq
        self.wordBank = Locators.selectWordsWordBank
        
    def clickByIndex(self,i):        
        self.wordBankElement[i].click()

    def clickByString(self,w):
        self.wordBankElement[self.wordBankList.index(w)].click()
    
    def solveKnown(self,trReq):
        print("is known")
        trList = str2list(trReq)
        for w in trList:
            print("w = "+w)
            self.clickByString(w)
            time.sleep(0.5)

    def solveUnknown(self):
        print("is unknown")
        self.clickByIndex(0)        
        print("word 1 selected")
        time.sleep(1)
    

    def solve(self):
        req = self.getReq()
        print("req = "+req)
        options = self.getWordBank()
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
                input() #check this case
                answ = cleanStringSpecialCharacters(str(self.wordBankList[0]))
                print("need lern a = " + trReq + ", b = " + req)
                learn(answ,req)
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

    def getWordBank(self):
        self.wordBankElement = self.driver.find_elements_by_css_selector(self.wordBank)
        print(len(self.wordBank))
        self.wordBankList = []
        print("getWordBank start")
        for w in self.wordBankElement:
            print((str(w.get_attribute("innerHTML")).lower()))
            self.wordBankList.append(str(w.get_attribute("innerHTML")).lower())
        print(self.wordBankList)        
        print("getWordBank end")
        return self.wordBankList