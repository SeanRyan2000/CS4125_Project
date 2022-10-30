import csv
import os

from CS4125_Project.model.Movie.ChildrensMovie import ChildrensMovie
from CS4125_Project.model.Movie.NormalMovie import NormalMovie
from CS4125_Project.model.Movie.SpecialMovie import SpecialMovie

MOVIE_CSV_PATH_STRING = str(os.path.abspath('..')) + '/csv_files/movies.csv'


def addNormalMovie(title, length, tickets):
    movie = NormalMovie(title, length, tickets)
    return movie

def addChildMovie(title, length, tickets):
    movie = ChildrensMovie(title, length, tickets)
    return movie

def addSpecialMovie(title, length, tickets):
    movie = SpecialMovie(title, length, tickets)
    return movie

def addMovieToCSV(movie):
    with open(MOVIE_CSV_PATH_STRING, 'a') as file:
        file.write("\n" + movie.getTitle() + "," + str(movie.getLength()) + "," + str(movie.getMovieType()) + "," + str(movie.getTickets()))
