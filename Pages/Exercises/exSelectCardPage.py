from locators import Locators
from globalFunctions import *
from exercisesPage import Exercises

class ExSelectCardPage(Exercises):

    def __init__(self,driver):
        super().__init__(driver)
        self.isCurrentPageElement = Locators.isSelectCard   # Overwrite isCurrentPageElement from parent class
        self.name = "selectCards"

        # Initialize objects (elements) of this page
        self.cards = Locators.selectCardCards
        self.textCard = Locators.selectCardTextCard
        self.req = Locators.selectCardReq
    
    def solve(self):
        req = self.getReq()
        print("req = "+req)
        options = self.getCardsName()
        print(options)

        trReq = translate(req,getTranslations()).lower()
        print("trReq = "+trReq)
        
        needLearn = False

        # Validate if translation exist
        if trReq != "":
            answIndex = options.index(trReq)
        else:
            needLearn = True
            answIndex = 0 
            trReq = options[0]
    
        print("answIndex = "+str(answIndex))
        self.clickCard(answIndex)
        self.clickButtonCheck()
        
        # Check if correct
        if(self.isCorrect()):
            print("*-*-*-*-*-*-* CORRECT *-*-*-*-*-*")            
            if(needLearn):
                print("need lern a = " + trReq + ", b = " + req)
                learn(trReq,req)           
        else:
            print("*-*-*-*-*-*-* INCORRECT *-*-*-*-*-*")
            answ = self.getCorrectAnswer()
            print("need lern a = " + answ + ", b = " + req)
            learn(answ,req)    

        print("click button check")
        self.clickButtonCheck()
    
    def getReq(self):
        return cleanStringSpecialCharacters(findBetweenQuotes(self.getTitle()))

    def getTitle(self):
        return str(self.driver.find_element_by_css_selector(self.req).get_attribute("innerHTML").lower())

    def getCardsName(self):
        self.readCards()
        txtCards = []
        for card in self.cards:
            txtCards.append(str(card.find_element_by_css_selector(self.textCard).get_attribute("innerHTML")).lower())
        return txtCards

    def readCards(self):
        self.cards = self.driver.find_elements_by_css_selector(self.cards)    

    def clickCard(self,index):
        self.cards[index].click()