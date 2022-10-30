import CS4125_Project.model.Movie.Movie as Movie

class NormalMovie(Movie.Movie):

    def __init__(self, title, length, tickets):
        super().__init__(title, length, tickets)

    def getMovieType(self):
        return "Normal"