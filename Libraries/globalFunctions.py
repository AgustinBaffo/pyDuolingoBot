import re
IMPLICIT_WAIT = 10

def findBetweenQuotes(s):
    return re.findall(r'"([^"]*)"', s)[0]


def translate(s,translations):
    for line in translations:
        if line[1] == s:
            return(line[0])  

    #The bot will check both columns until he learn how to recognize language when save file
    for line in translations:
        if line[0] == s:
            return(line[1])    
    return ""

def learn(a,b):
    f = open("./Translations/deu_spa.tra","a+",encoding='utf-8')
    f.write(str(a)+";"+str(b)+"\n")
    f.close()

def getTranslations():
    # Initialize translations
    db = open("./Translations/deu_spa.tra","r",encoding='utf-8')
    rawTranslations = db.read().split("\n")
    translations = list(map(lambda x: x.split(";"), rawTranslations))
    translations.pop()
    return translations

def cleanList(localList,strRemove):
    for s in strRemove:
        while s in localList:
            localList.remove(s)    
    return [x.lower() for x in localList]
def cleanListSpecialCharacters(localList):
    return cleanList(localList,[',','.',';'])

def cleanString(localString,strRemove):
    return(localString.translate({ord(i): None for i in strRemove}))
def cleanStringSpecialCharacters(localString):
    return cleanString(localString,',.;').lower()

def str2list(mystr):
    return re.sub("[^\w]", " ",  mystr).split()

def turnOnImplicitWait(driver):
    driver.implicitly_wait(IMPLICIT_WAIT)

def turnOffImplicitWait(driver):
    driver.implicitly_wait(0)

def setImplicitWait(driver,mode=True,seconds=IMPLICIT_WAIT):
    if mode==True:
        print("setting wait in "+str(seconds))
        driver.implicitly_wait(seconds)
    else:
        print("setting wait in 0")
        driver.implicitly_wait(0)