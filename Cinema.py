from ScreenList import ScreenList
 ##SETUP CINEMA MODEL##
class Cinema:
    SCREEN_LIST = ScreenList.setUp()

    ##Print all Screenings
    for s in SCREEN_LIST:
        print("Screen " + str(s.screenNum))
        print(s.printMovies(), "\n")