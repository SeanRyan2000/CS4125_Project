from flask import Flask, render_template, redirect, request, url_for
import os.path
import pandas

# from CS4125_Project.model.Register import *
# from Movie import Movie
from CS4125_Project.model.Register import validatePasswordStrength, emailValidator, ensurePasswordsAreEqual,\
    registerNewUser, checkIfEmailExists

TEMPLATES_PATH_STRING = str(os.path.abspath('..')) + '/templates'
STATIC_PATH_STRING = str(os.path.abspath('..')) + '/static'
CSV_PATH_STRING = str(os.path.abspath('..')) + '/file.csv'

app = Flask(__name__,
            template_folder=TEMPLATES_PATH_STRING,
            static_folder=STATIC_PATH_STRING
            )


def __init__(self, name):
    self.app = Flask(name)


@app.route('/movies')
def movie():
    # movieList = []

    # df = pandas.read_csv(CSV_PATH_STRING)

    # movieName = df['MOVIE'].tolist()
    # seatsLeft = df['TICKETS'].tolist()
    # for i in range(len(movieName)):
    #     movie = Movie(movieName[i], seatsLeft[i])
    #     movieList.append(movie)
    #     print(movieList)

    return render_template('movie.html')

@app.route('/')
def home():
    return render_template('home.html')

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


@app.route("/register", methods=['POST', 'GET'])
def registration():

    return render_template('register.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route("/registerUser", methods=['POST'])
def registerUser():

    if not validatePasswordStrength(str(request.form.to_dict().get('psw'))):
        error = 'password not strong enough'
        return render_template('register.html', error=error)

    if not emailValidator((request.form.to_dict().get('email'))):
        error = 'not a vaild email'
        return render_template('register.html', error=error)

    if not ensurePasswordsAreEqual(request.form.to_dict().get('psw'), request.form.to_dict().get('psw-repeat')):
        error = 'passwords not equal'
        return render_template('register.html', error=error)

    if checkIfEmailExists(request.form.to_dict().get('email')):
        error = 'email already in use'
        return render_template('register.html', error=error)

    registerNewUser(request.form.to_dict().get('email'), request.form.to_dict().get('psw'))

    return redirect('/home')

@app.route('/home')
def loginSuccessfully():

    return render_template('login_TEST_CLASS.html')

@app.errorhandler(404)
def not_found(e):

    # When a 404 not found error is thrown, this page will load.
    # TODO update this HTML page
    return render_template('page_not_found.html')