import csv
import os

from model.Movie.ChildrensMovie import ChildrensMovie
from model.Movie.StandardMovie import StandardMovie
from model.Movie.NewReleaseMovie import NewReleaseMovie
from model.Movie.Observable import Observable

MOVIE_CSV_PATH_STRING = str(os.path.abspath('..')) + '/csv_files/movies.csv'

observable = Observable()

def addNewReleaseMovie(title, length, tickets):
    movie = NewReleaseMovie(title, length, tickets)
    return movie

def addChildrensMovie(title, length, tickets):
    movie = ChildrensMovie(title, length, tickets)
    return movie

def addStandardMovie(title, length, tickets):
    movie = StandardMovie(title, length, tickets)
    return movie

def addMovieToCSV(movie):

    with open(MOVIE_CSV_PATH_STRING, 'a') as file:
        file.write("\n" + 
        movie.getMovieName() + "," + 
        str(movie.getMovieLength()) + "," + 
        str(movie.getMovieType()) + "," + 
        str(movie.getTicketsLeft()))

    # Observer design patter. Notify user when a new movie is added
    observable.notify_user()
