import CS4125_Project.model.Movie.Movie as Movie

class ChildrensMovie(Movie.Movie):

    def __init__(self, title, length, tickets):
        super().__init__(title, length, tickets)
        self.type = "childrens"

    def getMovieType(self):
        return self.type

    def __call__(self):
        return self

