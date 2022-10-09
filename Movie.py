class Movie:
    def __init__(self, title, length):
        self.title = title
        self.length = length

    ##Return Movie Title & Length
    def __str__(self) -> str:
        return "{}({})".format(self.title, self.getMovieLength())

    ##Get Movie Length in Hours & Minutes
    def getMovieLength(self):
        return "{}:{}".format(self.length // 60, str(self.length % 60).zfill(2))

p1 = Movie("Avatar", 123)
print(p1)