#Import modules and libs
import sys, os, pathlib
import time
from pprint import pprint
from selenium import webdriver
import unittest
import platform

OS_WIDNOWS = True if platform.system()=='Windows' else False

# Create paths
root = str(pathlib.Path(__file__).parent.parent)
sys.path.insert(0, root)
from routes import myRoutes
routes = myRoutes()

if OS_WIDNOWS:
    print("Running for Windows")
    routes.addPath("DRIVERS",routes.routes["ROOT"]+"\Drivers")
    routes.addPath("LIBRARIES",routes.routes["ROOT"]+"\Libraries")
    routes.addPath("TESTS",routes.routes["ROOT"]+"\Tests")
    routes.addPath("LOCATORS",routes.routes["ROOT"]+"\Locators")
    routes.addPath("PAGES",routes.routes["ROOT"]+"\Pages")
    routes.addPath("PAGES",routes.routes["ROOT"]+"\Pages\Execises")
    routes.addPath("TRANSLATIONS",routes.routes["ROOT"]+"\Translations")
    DRIVERS_PATH = routes.routes["DRIVERS"]
    CHROME_DRIVER_PATH = DRIVERS_PATH + r"/chromedriver.exe"
    
else:
    print("Running for Linux")
    routes.addPath("DRIVERS",routes.routes["ROOT"]+"/Drivers")
    routes.addPath("LIBRARIES",routes.routes["ROOT"]+"/Libraries")
    routes.addPath("TESTS",routes.routes["ROOT"]+"/Tests")
    routes.addPath("LOCATORS",routes.routes["ROOT"]+"/Locators")
    routes.addPath("PAGES",routes.routes["ROOT"]+"/Pages")
    routes.addPath("PAGES",routes.routes["ROOT"]+"/Pages/Execises")
    routes.addPath("TRANSLATIONS",routes.routes["ROOT"]+"/Translations")

# routes.printCreation()



driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
# Import my modules and clases
from Libraries.globalFunctions import *

from Pages.loginPage import LoginPage
from Pages.homePage import HomePage
from Pages.exercisesPage import Exercises
from Pages.Exercises.exSelectCardPage import ExSelectCardPage
from Pages.Exercises.exSelectWordsPage import ExSelectWordsPage
from Pages.Exercises.exListenTapPage import ExListenTap
from Pages.Exercises.exListenWritingPage import ExListenWriting
from Pages.Exercises.exSpeakingPage import ExSpeaking
from Pages.Exercises.exSelectSentence import ExSelectSentence
from Pages.Exercises.exWritingPage import ExWriting
from Pages.Exercises.exCompleteWordPage import ExCompleteWord
from Pages.Exercises.exCompleteWordWritingPage import ExCompleteWordWriting
from Pages.Exercises.exDuoSayHello import ExDuoSayHello
from Pages.Exercises.exFinalPage import ExFinalPage

IMPLICIT_WAIT = 10

class Solver(unittest.TestCase):
    def setUp(self):
        self.USERNAME = ""
        self.PASSWORD = ""
        self.driver = webdriver.Chrome(executable_path = CHROME_DRIVER_PATH)
        turnOnImplicitWait(self.driver)

    def tearDown(self):         # only when all test is completed. If you use tearDown(self) is for every test        
        self.driver.close()     #close tab
        self.driver.quit()      #close windows
        print("*-*-* COMPLETED! *-*-*")

    def test_login_valid(self):        
        driver = self.driver
        driver.get("https://www.duolingo.com/")
        # Login and home
        time.sleep(2)
        login = LoginPage(driver)
        login.clickStart()        
        time.sleep(2)
        login.enterUsername("agusbaffo@hotmail.com")
        login.enterPassword("bafferBot123")
        login.clickLogin()       
        time.sleep(2)

        self.play()   
    
    def play(self):
        driver = self.driver

        while(True):
            input()
            home = HomePage(driver)
            home.clickFirstAvailableLevel()
            input()
            self.playLevel()
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
            print("*-*-*-* END EXERCISE *-*-*-*-*")
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
            time.sleep(3)


    def playLevel(self):
        driver = self.driver
        while(True):
            time.sleep(4)
            exName = self.checkCurrentEx()
            print("\n\n---------------------------------------------------------")
            print(exName)
            print("---------------------------------------------------------\n\n")            
            if exName == "selectWords":
                print("is selectWords")
                ex = ExSelectWordsPage(driver)
                ex.solve()
                print("solved")
            elif exName == "selectCards":
                print("is selectCards")
                ex = ExSelectCardPage(driver)
                ex.solve()
                print("solved")
            elif exName == "writing":
                print("is writing")
                ex = ExWriting(driver)
                ex.solve()
                print("solved")
            elif exName == "selectSentence":
                print("is selectSentence")
                ex = ExSelectSentence(driver)
                ex.solve()
                print("solved")
            elif exName == "listenTap":
                print("is listenTap")
                ex = ExListenTap(driver)
                ex.solve()
                print("solved")
            elif exName == "listenWriting":
                print("is listenWriting")
                ex = ExListenWriting(driver)
                ex.solve()
                print("solved")
            elif exName == "speaking":
                print("is speaking")
                ex = ExSpeaking(driver)
                ex.solve()
                print("solved")
            elif exName == "completeWord":
                print("is completeWord")
                ex = ExCompleteWord(driver)
                ex.solve()
                print("solved")
            elif exName == "completeWordWriting":
                print("is completeWordWriting")
                ex = ExCompleteWordWriting(driver)
                ex.solve()
                print("solved")
            elif exName == "duoSayHello":
                print("is duoSayHello")
                ex = ExDuoSayHello(driver)
                ex.solve()
            elif exName == "final":
                print("is final")
                ex = ExFinalPage(driver)
                ex.solve()
                return
            else:
                print("\n\n\nunknown exercise")
                input()
            print("deleting")
            del ex
    
    def checkCurrentEx(self):
        # It tries 5 times waiting 2 seconds every time
        exList = self.getPageList()       
        for i in range(5):
            for ex in exList:
                if ex.isCurrentPage():
                    return ex.name
                print("name = " + ex.name)
            time.sleep(2)        
        return ""    # Means no name
    
    def getPageList(self):   
        driver = self.driver
        selectCards = ExSelectCardPage(driver)
        selectWords = ExSelectWordsPage(driver)
        listenTap = ExListenTap(driver)
        listenWriting = ExListenWriting(driver)
        speaking = ExSpeaking(driver)
        selectSentence = ExSelectSentence(driver)
        duoSayHello = ExDuoSayHello(driver)
        completeWord = ExCompleteWord(driver)
        writing = ExWriting(driver)
        completeWordWriting = ExCompleteWordWriting(driver)
        final = ExFinalPage(driver)
        exList = [selectCards,selectWords,listenTap,listenWriting,speaking,writing,selectSentence,completeWord,completeWordWriting,duoSayHello,final]
        return exList

if __name__ == '__main__':
    
    # Set username and password
    params = dict(arg.split('=') for arg in sys.argv[1:])
    if all (k in params for k in ('user','password')):
        user = params['user']
        password = params['password']
    else:
        print("Key 'user' or 'password' not found. Enter manually.")
        user = input("Username: ")
        password = input("Password: ")
        
    Solver.USERNAME = user
    Solver.PASSWORD = password

    unittest.main()
