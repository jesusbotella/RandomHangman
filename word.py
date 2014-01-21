import urllib2

class Word(object):
    """Class for word in game"""
    def __init__(self):
        super(Word, self).__init__()
        self.retrieveWord()
        self.wordStatus=set()

    def getWord(self):
        return self.word

    def retrieveWord(self):
        self.word=urllib2.urlopen("http://randomword.setgetgo.com/get.php").read().strip().upper()
        self.wordSet=set(self.word)

    def getWordStatus(self):
        returnValue=""
        for letter in self.word:
            if letter in self.wordStatus:
                returnValue=returnValue+letter+" "
            else:
                returnValue=returnValue+"_ "
        return returnValue

    def matchLetter(self,letter):
        if letter in self.wordSet:
            self.wordStatus.add(letter)
            return True
        else:
            return False

    def matchWord(self):
        if len(self.wordSet.difference(self.wordStatus))==0:
            return True
        else:
            return False
