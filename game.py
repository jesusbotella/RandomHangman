from word import Word

class Game(object):
    """Class for Managing Hangman Random Game"""
    def __init__(self, playersList):
        super(Game, self).__init__()
        self.playersList = playersList
        self.correct=False
        self.playerTurn = 0
        self.failures = 0
        self.usedLetters=set()

    def run(self):
        print "\nGetting word from Internet..."
        self.word=Word()

        while(self.correct==False and self.failures < 6):
            self.printState()
            letter=raw_input("\nWhich letter do you choose, "+str(self.playersList[self.playerTurn]['name'])+"?\n").upper()
            if self.word.matchLetter(letter):
                print "The word contains the letter '"+letter+"'\n"
            else:
                print "Oh, the word doesn't contain the letter '"+letter+"'\n"
                self.failures=self.failures+1
            self.usedLetters.add(letter)
            self.correct=self.word.matchWord()
            if self.correct != True: self.playerTurn=(self.playerTurn+1)%len(self.playersList)

        self.printState()
        if self.correct == True:
            print "Congratulations! "+str(self.playersList[self.playerTurn]['name'])+" have guessed the word! :)"
        else:
            print "Oh no! You haven't guessed the word :(\nThe word was "+self.word.getWord()+"\n"

    def printState(self):
        print "--------\n|      |"
        print "|     ",
        if self.failures > 0 : print "O"
        else: print
        print "|   ",
        if self.failures > 1 :
            print "/",
            if self.failures > 2 :
                print "|",
                if self.failures > 3 :
                    print "\\"
                else: print
            else: print
        else: print
        print "|    ",
        if self.failures > 4 :
            print "/",
            if self.failures > 5 :
                print "\\"
            else: print
        else: print
        print "|                "+self.word.getWordStatus()+"\n-"
        print "Used Letters:",self.getUsedLettersSTR()

    def getUsedLettersSTR(self):
        returnValue=""
        for letter in self.usedLetters:
            returnValue=returnValue+letter+" "
        return returnValue
