from locators import Locators
import time


class HomePage():
    def __init__(self,driver):        
        self.driver = driver
        self.MAX_CROWNS = 5

        #Initialize objects (elements) of this page
        self.levelCS = Locators.levelCS
        self.buttonLevelStartCS = Locators.buttonLevelStartCS
        self.levelCrownsCS = Locators.levelCrownsCS
        self.home = Locators.homeCS

    def clickFirstAvailableLevel(self):
        print("*-*-* clickFirstAvailableLevel *-*-*")
        self.goHome() # This close possible existing windows
        levels = self.getAllAvailableLevels() 
        for l in levels:
            haveCorwns = len(l.find_elements_by_css_selector(self.levelCrownsCS))>0
            print("haveCorwns = " + str(haveCorwns))
            if haveCorwns: # if have "crown element"
                crowns = int(l.find_element_by_css_selector(self.levelCrownsCS).get_attribute("innerHTML"))
                if crowns < self.MAX_CROWNS:
                    self.playLevel(l)
                    print("crowns = " + str(crowns) + " => play it ")
                    break
                else:
                    continue    # if have 5 crowns, do not play it
            else:               # if element if enable but it don't have crowns, play it
                self.playLevel(l)
                print("don't have crowns => play it ")
                break
        # remember last index ? -> do not search any time duoBot finishes an exercise
    
    def goHome(self):
        self.driver.find_element_by_css_selector(self.home).click()
        time.sleep(4)

    def getAllAvailableLevels(self):
        return self.driver.find_elements_by_css_selector(self.levelCS)
    
    def playLevel(self,level):
        print("playLevel")
        level.click()
        time.sleep(1)
        print("level clicked")
        self.driver.find_element_by_css_selector(self.buttonLevelStartCS).click()
        print("start clicked")