import model.Movie.Movie as Movie

class SpecialMovie(Movie.Movie):

    def __init__(self, title, length, tickets):
        super().__init__(title, length, tickets)

    def getMovieType(self):
        return "Special"