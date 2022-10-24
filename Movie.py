from Ticket import Ticket

class Movie:
    def __init__(self, title, length, t, tickets):
        self.title = title
        self.length = length
        self.t = t
        self.tickets = tickets
        self.screenNum = 0

    ##Get Number of Tickets Left
    def getTicketsLeft(self):
        return self.tickets

    ##Update Number of Tickets for Movie
    def setTicketsLeft(self, tickets):
        self.tickets = tickets

    ##Set the Screen Movie is being Played in
    def setScreenNum(self, screenNum):
        self.screenNum = screenNum
 
    ##Return Movie Title & Length
    def printMovie(self) -> str:
        return "{} ({})".format(self.title, self.getMovieLength())

    ##Get Movie Length in Hours & Minutes
    def getMovieLength(self):
        return "{}:{}".format(self.length // 60, str(self.length % 60).zfill(2))