from Screen import Screen
from Movie import Movie
import csv

 ##SETUP CINEMA MODEL##
class Cinema:
    NUMBER_OF_SCREENS = 8
    MOVIES_PER_SCREEN = 4
    SCREEN_LIST = []
    MOVIE_LIST = {}

    #Setup Screens 1-8
    for x in range(NUMBER_OF_SCREENS):
        s = Screen(x + 1)
        SCREEN_LIST.append(s)

    ##Read in Movie Data
    with open('csv_files/movies.csv','r') as movies:
        MOVIE_LIST = csv.DictReader(movies)

    #Setup Movies for each Screen
        i = screen = 0
        for m in MOVIE_LIST:
            SCREEN_LIST[screen].movies[i] = Movie(m["TITLE"],int(m["LENGTH"]),m["TYPE"])

            i += 1
            if(i == MOVIES_PER_SCREEN): 
                screen += 1 
                i = 0
    
    ##Print all Screenings
    for s in SCREEN_LIST:
        print("Screen " + str(s.screenNum))
        print(s.printMovies(), "\n")