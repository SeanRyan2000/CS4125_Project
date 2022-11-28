import os
import pandas as pd
from flask import session

from model.Movie import NewReleaseMovie, ChildrensMovie, StandardMovie

MOVIE_CSV_PATH_STRING = str(os.path.abspath('..')) + '/csv_files/movies.csv'

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

    def createMovieFromCSV(self, movieName):
        movie = None
        print(f'ses = {session.get("movie")}')
        # read movies csv file with pandas
        dataFrame = pd.read_csv(MOVIE_CSV_PATH_STRING, usecols=['TITLE', 'LENGTH', 'TYPE', 'TICKETS'])
        # find title in csv file
        for title in dataFrame.values:
            if title[0] == movieName:
                if title[2] == 'new':
                    movie = NewReleaseMovie.NewReleaseMovie(title[0], title[1], title[3])
                elif title[2] == 'childrens':
                    movie = ChildrensMovie.ChildrensMovie(title[0], title[1], title[3])
                elif title[2] == 'standard':
                    movie = StandardMovie.StandardMovie(title[0], title[1], title[3])

        return movie
