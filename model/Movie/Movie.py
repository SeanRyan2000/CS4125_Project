from abc import ABC, abstractmethod



class Movie(ABC):
    def __init__(self, title, length, tickets):
        self.title = title
        self.length = length
        self.type = ""
        self.tickets = tickets

    def setMovieName(self, title):
        self.title = title

    def getMovieName(self):
        return str(self.title)

    def getFormattedMovieLength(self):
        return "{}:{}".format(self.length // 60, str(self.length % 60).zfill(2))

    def getMovieLength(self):
        return self.length

    @abstractmethod
    def getMovieType(self):
        pass

    def getTicketsLeft(self):
        return self.tickets

    def setTicketsLeft(self, numberOfSeats):
        return self.tickets - numberOfSeats

    def printMovie(self) -> str:
        return "{} ({})".format(self.title, self.getFormattedMovieLength())

