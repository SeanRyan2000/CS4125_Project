class Ticket:
    def __init__(self, movie, ticketType):
        self.movieName = movie.getMovieName()
        self.movieLength = movie.getMovieLength()
        self.movieType = movie.getMovieType()
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

    def getMovieInfo(self) -> str:
        return "{} ({})".format(self.movieName, self.movieLength)