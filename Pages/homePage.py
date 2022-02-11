from locators import Locators
import time
from selenium import webdriver

class HomePage():
    def __init__(self,driver):        
        self.driver = driver
        self.MAX_CROWNS = 5

        #Initialize objects (elements) of this page
        self.levelCS = Locators.levelCS
        self.levelIconCS = Locators.levelIconCS
        self.buttonLevelStartCS = Locators.buttonLevelStartCS
        self.levelCrownsCS = Locators.levelCrownsCS
        self.home = Locators.homeCS

    def clickFirstAvailableLevel(self):
        print("clicking first available level *-*-*")
        self.goHome() # This closes possible existing windows
        levels = self.getAllAvailableLevels()
        for l in levels:
            haveCorwns = len(l.find_elements_by_css_selector(self.levelCrownsCS))>0
            # print("haveCorwns = " + str(haveCorwns))
            if haveCorwns: # if "crown element" exists
                crowns = int(l.find_element_by_css_selector(self.levelCrownsCS).get_attribute("innerHTML"))
                if crowns < self.MAX_CROWNS:
                    print("crowns = " + str(crowns) + " => play it ")
                    self.playLevel(l)
                    break
                else:
                    continue    # if have 5 crowns, do not play it
            else:               # if element if enable but it don't have crowns, play it
                print("level doesn't have crowns => play it ")
                self.playLevel(l)
                break
        # TODO: remember last index ? -> do not search any time duoBot finishes an exercise
    
    def goHome(self):
        self.driver.find_element_by_css_selector(self.home).click()
        time.sleep(4)

    def getAllAvailableLevels(self):
        return self.driver.find_elements_by_css_selector(self.levelCS)
    
    def playLevel(self,level):
        webdriver.ActionChains(self.driver).move_to_element(level).click(level).perform()
        time.sleep(1)
        self.driver.find_element_by_css_selector(self.buttonLevelStartCS).click()