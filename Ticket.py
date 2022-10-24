class Ticket:
    def __init__(self, movieName, movieLength, screenNum, price):
        self.movieName = movieName
        self.movieLength = movieLength
        self.screenNum = screenNum
        self.price = price
    
    ##Get the Price for Ticket
    def getTicketPrice(self):
        return self.price

    ##Print Ticket Information
    def printTicketInfo(self):
        print("Movie: ", self.movieName)
        print("Time: ", self.movieLength)
        print("Screen: ", self.screenNum)
        print("Price: ", self.price)
