class Locators():

    # LoginPage    
    buttonStartXpath = "//a[contains(@data-test, 'have-account')]"
    textboxUsernameXpath = "//input[contains(@data-test, 'email-input')]"
    textboxPasswordXpath = "//input[contains(@data-test, 'password-input')]"
    buttonLoginXpath = "//button[contains(@data-test, 'register-button')]"

    # HomePage
    levelCS = "div[data-test='skill']"                  # any level
    levelIconCS = "div[data-test='skill-icon']"         # any level
    levelCrownsCS = "div[data-test='level-crown']"      # level with at leas 1 crown (inner html return number of crowns)
    buttonLevelStartCS = "button[data-test='start-button']" 
    levelTestCS = "div[data-test='checkpoint-badge']"
    homeCS = "a[data-test='home-nav']"

    # General in exercises (by CSS Selector)
    buttonQuit = "button[data-test='quit-button']"
    header = "h1[data-test='challenge-header']"
    buttonSkip = "button[data-test='player-skip']"
    buttonCheck = "button[data-test='player-next']"
    
    answStatus = "div[data-test*='blame']"
    isIncorrectAnsw = "div[data-test*='blame-incorrect']"
    isCorrectAnsw = "div[data-test*='blame-correct']"
    correctAnsw = "div[data-test*='blame-incorrect'] h2+div"
    toggleKeyboard = "button[data-test='player-toggle-keyboard']"

    # IsCurrrentPage
    isSelectWords1 = "div[data-test='challenge challenge-translate']"
    isSelectWords2 = "div[data-test='word-bank']"
    isWriting1 = "div[data-test='challenge challenge-translate']"
    isWriting2 = "textarea[data-test='challenge-translate-input']"
    isSelectCard = "div[data-test='challenge challenge-select']"
    isListenTap = "div[data-test='challenge challenge-listenTap']"
    isListenWriting = "div[data-test='challenge challenge-listen']"
    isSelectSentence = "div[data-test='challenge challenge-judge']"
    isCompleteWord = "div[data-test='challenge challenge-form']"
    isSpeaking = "div[data-test='challenge challenge-speak']"
    isCompleteWordWriting = "div[data-test='challenge challenge-completeReverseTranslation']"
    isFinalPage = "div[data-test='player-end-carousel']"

    # FinalPage (by CSS Selector)
    buttonNoThanksToPlus = "button[data-test='no-thanks-to-plus']"

    # Writing (by CSS Selector)
    writingReq = "span[data-test='hint-sentence'] div"
    writingTextArea = "textarea[data-test='challenge-translate-input']"

    # SelectCard (by CSS Selector)
    selectCardReq = "h1[data-test='challenge-header'] span"
    selectCardCards = "label[data-test='challenge-choice-card']"
    selectCardTextCard = "span[style*='font-size:']"

    # SelectWord (by CSS Selector)
    selectWordsReq = "span[data-test='hint-sentence'] div"
    selectWordsWordBank = "div[data-test='word-bank'] button"

    # SelectSentence (by CSS Selector)
    selectSentenceReq = "div[data-test='challenge challenge-judge'] div div div"
    selectSentenceOptions = "div[data-test='challenge-choice']"
    selectSentenceOptionsInput = "input[data-test='challenge-choice-card-input']"
    selectSentenceOptionsText = "div[data-test='challenge-judge-text']"

    # CompleteWord (by CSS Selector)
    completeWordReq = "div[data-test='challenge-form-prompt']"
    completeWordOptions = "label[data-test='data-test='challenge-choice']"
    completeWordOptionsInput = "input[data-test='challenge-choice-card-input']"
    completeWordOptionsText = "div[data-test='challenge-judge-text']"
    
    # CompleteWordWriting (by CSS Selector)
    completeWordWritingReq = "span[data-test='hint-sentence'] div"
    completeWordWritingInput = "input[data-test='challenge-translate-input']"           #before press toggle button
    completeWordWritingTextArea = "textarea[data-test='challenge-translate-input']"     #after press toggle button