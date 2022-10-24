from Screen import Screen
from Movie import Movie
import csv

class ScreenList:
    def setUp():
        ##Constants
        NUMBER_OF_SCREENS = 8
        MOVIES_PER_SCREEN = 4
        SCREEN_LIST = []

        ##Setup Screens 1-8
        for x in range(NUMBER_OF_SCREENS):
            s = Screen(x + 1)
            SCREEN_LIST.append(s)

        ##Read in Movie Data
        with open('csv_files/movies.csv','r') as movies:
            movieList = csv.DictReader(movies)

        #Setup Movies for each Screen
            i = screen = 0
            for m in movieList:
                SCREEN_LIST[screen].movies[i] = Movie(m["TITLE"],int(m["LENGTH"]),m["TYPE"], int(m["TICKETS"]))
                SCREEN_LIST[screen].movies[i].setScreenNum(screen + 1)

                i += 1
                if(i == MOVIES_PER_SCREEN): 
                    screen += 1 
                    i = 0

        return SCREEN_LIST