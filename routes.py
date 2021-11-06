import sys, pathlib

class myRoutes:
    def __init__(self):
        self.routes = {}
        self.order = 1  # This is to add element ordered

        # Always add root to path
        self.addDic("ROOT",str(pathlib.Path(__file__).parent))

        # If you want to add to path and dic some path in startup
        # self.addPath("TESTS",self.routes["ROOT"]+"\Tests")
        # self.addPath("LOCATORS",self.routes["ROOT"]+"\Locators")
        
        # self.printCreation()
    
    def addDic(self,key,value):
        self.routes[key] = value

    def addPath(self,key,value):
        self.routes[key] = value
        sys.path.insert(self.order, self.routes[key])
        self.order+=1

    def printCreation(self):
        from pprint import pprint
        print("-------- route created --------")
        pprint(self.routes)
        print("-------------------------------")
