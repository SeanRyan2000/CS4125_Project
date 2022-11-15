class Ticket:
    def __init__(self, movie, ticketType):
        self.movieName = movie.getMovieName()
        self.movieLength = movie.getMovieLength()
        self.movieType = movie.getMovieType()
        self.screenNum = movie.getScreenNum()
        self.ticketType = ticketType
    
    ##Get the Price for Ticket
    def getPrice(self):
        price = 0
        if self.ticketType == "kids":
            price = 8
        elif self.ticketType == "student":
            price = 10
        elif self.ticketType == "adult":
            price = 12

        if self.movieType == "childrens":
            price = price * 0.8
        elif self.movieType == "new":
            price = price * 1.2

        return price

    ##Print Ticket Information
    def returnTicketInfo(self):
        return "Movie: {}\n Time: {}\n Type: {}\n Screen: {}\n Ticket: {}\n Price: {}\n".format(self.movieName, self.movieLength, self.movieType, self.screenNum, self.ticketType, self.price)