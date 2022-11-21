from model.Movie import NewReleaseMovie, ChildrensMovie, StandardMovie

from model.Admin.AddMovie import addMovieToCSV
from model import Movie

import os

MOVIE_CSV_PATH_STRING = str(os.path.abspath('..')) + '/csv_files/movies.csv'
import pandas as pd

class MovieFactory:

    def createMovie(self, request):

        movie = None

        if request.get('type') == 'NewReleaseMovie':
            movie = NewReleaseMovie.NewReleaseMovie(request.get('title'), request.get('movie_length'), request.get('tickets'))
        elif request.get('type') == 'ChildrensMovie':
            movie = ChildrensMovie.ChildrensMovie(request.get('title'), request.get('movie_length'), request.get('tickets'))
        elif request.get('type') == 'StandardMovie':
            movie = StandardMovie.StandardMovie(request.get('title'), request.get('movie_length'), request.get('tickets'))

        return movie


class Observable():
    
    def __init__(self):

        email = pd.read_csv(MOVIE_CSV_PATH_STRING)
  
        self.userEmail = email['EMAIL'].tolist()
 
        
    def unregister(self, user):
        self.userEmail.remove(user.getUserEmail())
     
    def notify_user(self):
        
        if(addMovieToCSV(Movie)):
            
            for user in self.userEmail:
                user.update(self)