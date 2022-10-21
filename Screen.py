import csv
class Screen():
    def __init__(self, screenNum):
        self.screenNum = screenNum
        self.movies = [None] * 4

    ##Get Screen Number
    def getScreenNum(self):
        return self.screenNum

    ##Print List of Movies for Screen
    def printMovies(self):
        for m in self.movies:
            print(m.printMovie())

    ##Print 'Screen X'
    def __str__(self):
        return "Screen " + str(self.screenNum)
