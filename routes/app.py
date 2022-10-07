from flask import Flask, render_template, redirect, request
import os.path
import pandas
from Movie import Movie

TEMPLATES_PATH_STRING = str(os.path.abspath('..'))+'/templates'
STATIC_PATH_STRING = str(os.path.abspath('..'))+'/static'
CSV_PATH_STRING = str(os.path.abspath('..'))+'/file.csv'

app = Flask(__name__,
            template_folder=TEMPLATES_PATH_STRING,
            static_folder=STATIC_PATH_STRING
            )


def __init__(self, name):
    self.app = Flask(name)


@app.route('/movies')
def hello_world():
    movieList = []

    df = pandas.read_csv(CSV_PATH_STRING)

    movieName = df['MOVIE'].tolist()
    seatsLeft = df['TICKETS'].tolist()
    for i in range(len(movieName)):
        movie = Movie(movieName[i], seatsLeft[i])
        movieList.append(movie)
        print(movieList)

    return render_template('Movie.html', movieList=movieList)

@app.route("/test", methods=['POST'])
def buy_ticket_for_movie():

    df = pandas.read_csv(CSV_PATH_STRING)
    movieName = df['MOVIE'].tolist()

    # Check which button was clicked on the movies page by reading the request form and getting the movie name from that
    # Finding the column index of the movie in the CSV file
    index = movieName.index(list(request.form.to_dict())[0])

    # Decrease the ticket amount when a ticket is bought and update the CSV file
    df.at[index, 'TICKETS'] = df.at[index, 'TICKETS'] - 1
    df.to_csv(CSV_PATH_STRING, index=False)

    return redirect('/movies')
