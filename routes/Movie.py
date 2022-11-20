import pandas as pd
from model.Admin.AddMovie import addMovieToCSV
from routes.app import movie

import os
MOVIE_CSV_PATH_STRING = str(os.path.abspath('..')) + '/csv_files/movies.csv'

class Movie:
    def __init__(self, title, length, t, tickets):
        self.title = title
        self.length = length
        self.type = ""
        self.tickets = tickets
        self.screenNum = 0
        
        email = pd.read_csv(MOVIE_CSV_PATH_STRING)
  
        self.userEmail = email['EMAIL'].tolist()
 
    def register(self, user):
        self.userEmail.append(user.getUserEmail())  
        
    def unregister(self, user):
        self.userEmail.remove(user.getUserEmail())
     
    def notify_user(self, message):
        
        if(addMovieToCSV(movie)):
            
            for user in self.userEmail:
                user.update(self, message)

    def getTicketsLeft(self):
        return self.tickets

    def setTicketsLeft(self, numberOfSeats):
        return self.tickets - numberOfSeats

    def setScreenNum(self, screenNum):
        self.screenNum = screenNum

    def setMovieName(self, movieName):
        self.title = movieName

    def getName(self):
        return str(self.movie_name)

    def printMovie(self) -> str:
        return "{} ({})".format(self.title, self.getMovieLength())

    def getMovieLength(self):
        return "{}:{}".format(self.length // 60, str(self.length % 60).zfill(2))
