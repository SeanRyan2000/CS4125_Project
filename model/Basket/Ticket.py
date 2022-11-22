class Ticket:        
    def __init__(self, movie, ticketType):
        self.movieName = movie.getMovieName()
        self.movieLength = movie.getFormattedMovieLength()
        self.movieType = movie.getMovieType()
        self.ticketType = ticketType
        self.price = 0

    def getDescription(self):
        return "[{}] {} ({})".format(self.movieType.capitalize(), self.movieName, self.movieLength)

    #Get the Price for Ticket
    def getPrice(self):
        if self.ticketType == "kids":
            self.price = 8
        elif self.ticketType == "student":
            self.price = 10
        elif self.ticketType == "adult":
            self.price = 12

        if self.movieType == "childrens":
            self.price = self.price * 0.8
        elif self.movieType == "new":
            self.price = self.price * 1.2
        
        return self.price