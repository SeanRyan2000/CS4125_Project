class Ticket:
    def __init__(self, movieName, movieType, movieLength, numberOfTickets, ticketType, price):
        self.movieName = movieName
        self.movieType = movieType
        self.movieLength = movieLength
        self.numberOfTickets = numberOfTickets
        self.ticketType = ticketType
        self.price = price

    def getMoviePrice(self):
        # return price with two decimal places
        return "{:.2f}".format(self.price)

    def getDescription(self):
        return "[{}] {}".format(self.movieName, self.ticketType)

    # Get the Price for Ticket
    def getPrice(self):
        if self.ticketType == "Child":
            self.price = 8
        elif self.ticketType == "Student":
            self.price = 10
        else:
            self.price = 12

        if self.movieType == "childrens":
            self.price = self.price * 0.8
        elif self.movieType == "new":
            self.price = self.price * 1.2

        return self.price

    def __call__(self):
        return self
