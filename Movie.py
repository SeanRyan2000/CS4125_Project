class Movie:
    def __init__(self, title, length, t):
        self.title = title
        self.length = length
        self.t = t

    ##Return Movie Title & Length
    def printMovie(self) -> str:
        return "{} ({})".format(self.title, self.getMovieLength())

    ##Get Movie Length in Hours & Minutes
    def getMovieLength(self):
        return "{}:{}".format(self.length // 60, str(self.length % 60).zfill(2))