from flask import Flask, render_template, redirect, request, url_for, session
import os.path
import pandas as pd
import csv
import os, sys

currDir = os.path.dirname(os.path.realpath(__file__))
rootDir = os.path.abspath(os.path.join(currDir, '..'))
if rootDir not in sys.path: # add parent dir to paths
    sys.path.append(rootDir)

from ..model.Basket.Basket import Basket, BasketEmpty
from ..model.Basket.Concessions.AddOns import AddIceCream, AddHotDog, AddDrink, AddSweets
from ..model.Basket.Concessions.Popcorn import Popcorn, LargePopcorn, RegularPopcorn
from ..model.Basket.Ticket import Ticket
from ..model.Authentication.Register import validatePasswordStrength, emailValidator, ensurePasswordsAreEqual, registerNewUser, checkIfEmailExists
from ..model.Authentication.SignIn import verifyEmailAndPassword, checkEmailExists, signInUser
from ..model.Movie import MovieFactory
from ..model.Basket import TicketFactory
from ..model.Basket.Concessions.ConcessionFactory import ConcessionFactory
from ..model.Admin.AddMovie import addNewReleaseMovie, addChildrensMovie, addStandardMovie, addMovieToCSV

movieFactory = MovieFactory.MovieFactory()
concessionFactory = ConcessionFactory()

TEMPLATES_PATH_STRING = str(os.path.abspath('..')) + '/templates'
STATIC_PATH_STRING = str(os.path.abspath('..')) + '/static'
MOVIE_CSV_PATH_STRING = str(os.path.abspath('..')) + '/csv_files/movies.csv'

app = Flask(__name__,
            template_folder=TEMPLATES_PATH_STRING,
            static_folder=STATIC_PATH_STRING
            )
app.secret_key = 'secret key ahh'

myBasket = Basket(BasketEmpty())

def __init__(self, name):
    self.app = Flask(name)

# reading the data in the csv file

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/movies')
def movie():
    
        df = pd.read_csv(MOVIE_CSV_PATH_STRING, usecols=['TITLE', 'TICKETS'])
        movieNameAndTicket = df.set_index('TITLE')['TICKETS'].to_dict()
        return render_template('Movie.html',  movieNameAndTicket=movieNameAndTicket)

@app.route('/buyTicketScreen', methods=['POST'])
def buyTicketScreen():
    myBasket.clearBasket()
    movie = request.form.to_dict().get('movieName')
    # add movie name to session so that it can be used in the buyTicket function
    session['movie'] = movie
    print(session['movie'])
    return render_template('buyTicketScreen.html', moivieName=movie)

@app.route('/buyTicket', methods=['POST'])
def buyTicket():

    movie = movieFactory.createMovieFromCSV(session.get('movie'))
    print(session.get('movie'))
    ticket = Ticket(movie.getMovieName(), movie.getMovieType(), movie.getMovieLength(), 0, request.form.get('type'), 0)
    # TicketFactory.getTicketPrice(ticket)
    print('tickets ', request.form.get('tickets'))
    ticket.numberOfTickets = int(request.form.get('tickets'))
    ticket.price = ticket.getPrice() * int(request.form.get('tickets'))
    print('ticket price ', ticket.price)
    myBasket.addItem(ticket)


    # use ticket in addOns function

    session['ticket'] = ticket.__dict__ # to access the ticket object in addOns page
    return render_template('basket.html', ticket=ticket)

@app.route('/addOns', methods=['POST'])
def addOns():

    print(session.get('ticket'))
    return render_template('addOns.html', ticket=session.get('ticket'))

@app.route('/buyAddOns', methods=['POST'])
def buyAddOns():

    largePopcorn = LargePopcorn(request.form.get('large'))
    regularPopcorn = RegularPopcorn(request.form.get('regular'))
    if int(largePopcorn.getQuantity()) > 0:
        largePopcorn = AddIceCream(AddHotDog(AddDrink(largePopcorn)))
        myBasket.addItem(largePopcorn)


    if int(regularPopcorn.getQuantity()) > 0:
        regularPopcorn = AddSweets(AddDrink(regularPopcorn))
        myBasket.addItem(regularPopcorn)




    # print('\n\n\n\n\n\n\n\n\n\n\n\n\n\nBASKET: ', myBasket.viewBasket())
    string = myBasket.formattedString()
    print('SRTINTG', string)
    return session.get('formattedString')
    # return myBasket.viewBasket()
    # return render_template('final_basket.html', basket=myBasket)


@app.route('/')
def home():
    return render_template('home.html')

@app.route("/register", methods=['POST', 'GET'])
def registration():

    return render_template('register.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/signInUser', methods=['POST'])
def validateSignIn():

    if not checkEmailExists((request.form.to_dict().get('email'))):
        error = 'Email doesn\'t exist'
        return render_template('signin.html', error=error)
    if not verifyEmailAndPassword((request.form.to_dict().get('email')), (request.form.to_dict().get('password'))):
        error = 'Password incorrect'
        return render_template('signin.html', error=error)

    session['signin'] = True
    print(session['signin'])
    return render_template('home.html', data=session['signin'])

@app.route('/logout')
def logout():
    session['signin'] = False
    return render_template('home.html')

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

    return render_template('base.html')

@app.errorhandler(404)
def not_found(e):

    # When a 404 not found error is thrown, this page will load.
    # TODO update this HTML page
    return render_template('page_not_found.html')

@app.errorhandler(500)
def internal_error(e):

    # TODO create a pop up that displays this on the page rather than a new page being loaded
    return 'Internal server error.'

@app.route('/admin')
def admin():
    return render_template('admin_dashboard.html')

@app.route('/admin/add_movie', methods=['POST'])
def add_movie():

    if len(request.form.to_dict()) != 0:
        movieToBeAdded = movieFactory.createMovie(request.form.to_dict())
        addMovieToCSV(movieToBeAdded)
    else:
        print('error')

    return redirect('/admin')