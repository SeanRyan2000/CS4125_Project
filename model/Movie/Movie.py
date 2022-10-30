import abc


class Movie(abc.ABC):

    def __init__(self, title, length, tickets):
        self.title = title
        self.length = length
        self.tickets = tickets

    def getTitle(self):
        return self.title

    def getLength(self):
        return self.length

    def getTickets(self):
        return self.tickets

    def setTickets(self, tickets):
        self.tickets = tickets

