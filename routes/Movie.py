class Movie:
    movie_name = ''
    seats_left = 0

    def __init__(self, m, t):
        self.movie_name = m
        self.seats_left = t

    def alter_seats_left(self, numberOfSeats):
        return self.seats_left-numberOfSeats

    def setMovieName(movieName):
        movie_name = movieName

    def getName(self):
        return str(self.movie_name)

    def toString(self):
        return f'Movie Name: {self.movie_name}. Tickets left: {self.seats_left}'

