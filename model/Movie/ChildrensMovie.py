import Movie as movie

class ChildrensMovie(movie):

    def __init__(self, title, length, tickets):
        super().__init__(title, length, tickets)
        self.type = "childrens"

    def getMovieType(self):
        return self.type

    def __call__(self):
        return self

