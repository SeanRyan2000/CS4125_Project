from model.Movie import NewReleaseMovie, ChildrensMovie, StandardMovie

from model.Admin.AddMovie import addMovieToCSV
from model import Movie
import pytest

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


def test_createMovie():
    movieFactory = MovieFactory()
    movie = movieFactory.createMovie({'type': 'NewReleaseMovie', 'title': 'Test', 'movie_length': 120, 'tickets': 100})
    assert isinstance(movie, Movie.NewReleaseMovie.NewReleaseMovie)


