import pandas as pd
import abc

class Movie(abc.ABC):

    def __init__(self, title, length, tickets):
        self.movie_name = title
        self.length = length
        self.type = ""
        self.tickets = tickets
        self.screenNum = 0

    def getTicketsLeft(self):
        return self.tickets

    def setTicketsLeft(self, numberOfSeats):
        return self.tickets - numberOfSeats

    def setScreenNum(self, screenNum):
        self.screenNum = screenNum

    def setMovieName(self, movieName):
        self.title = movieName

    def getName(self):
        return str(self.movie_name)

    def printMovie(self) -> str:
        return "{} ({})".format(self.title, self.getMovieLength())

    def getMovieLength(self):
        return self.length
