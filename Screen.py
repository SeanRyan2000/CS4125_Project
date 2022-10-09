class Screen():
    def __init__(self, screenNum):
        self.screenNum = screenNum

    def getScreenNum(self):
        return self.screenNum

    def printScreen(self):
        return "Screen " + str(self.screenNum)
