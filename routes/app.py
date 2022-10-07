from flask import Flask, render_template, redirect, request, url_for
import pandas
from Movie import Movie

app = Flask(__name__,
            template_folder='/home/andrew/PycharmProjects/cs4125/CS4125-Project/templates',
            static_folder='/home/andrew/PycharmProjects/cs4125/CS4125-Project/static')


def __init__(self, name):
    self.app = Flask(name)


@app.route('/movies')
def hello_world():
    movieList = []

    df = pandas.read_csv('/home/andrew/PycharmProjects/cs4125/CS4125-Project/file.csv')

    movieName = df['MOVIE'].tolist()
    seatsLeft = df['TICKETS'].tolist()
    for i in range(len(movieName)):
        movie = Movie(movieName[i], seatsLeft[i])
        movieList.append(movie)
        print(movieList)

    return render_template('Movie.html', movieList=movieList)


@app.route("/test", methods=['POST'])
def buy_ticket_for_movie():

    df = pandas.read_csv('/home/andrew/PycharmProjects/cs4125/CS4125-Project/file.csv')
    movieName = df['MOVIE'].tolist()

    index = movieName.index(list(request.form.to_dict())[0])

    df.at[index, 'TICKETS'] = df.at[index, 'TICKETS'] - 1
    df.to_csv('/home/andrew/PycharmProjects/cs4125/CS4125-Project/file.csv', index=False)

    return redirect('/movies')
