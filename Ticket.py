class Ticket:
    def __init__(self, movieName, movieLength, screenNum, t, price):
        self.movieName = movieName
        self.movieLength = movieLength
        self.screenNum = screenNum
        self.type = t
        self.price = price
    
    ##Get the Price for Ticket
    def getTicketPrice(self):
        return self.price

    ##Print Ticket Information
    def returnTicketInfo(self):
        return "Movie: {}\n Time: {}\n Screen: {}\n Type: {}\n Price: {}\n".format(self.movieName, self.movieLength, self.screenNum, self.type, self.price)
