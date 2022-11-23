from flask import Flask, render_template, redirect, request, url_for, session, jsonify, render_template
from decouple import config
import os.path
import pandas 
import pandas as pd
import csv
import stripe

import os, sys
currDir = os.path.dirname(os.path.realpath(__file__))
rootDir = os.path.abspath(os.path.join(currDir, '..'))
if rootDir not in sys.path: # add parent dir to paths
    sys.path.append(rootDir)


# print(rootDir)
# from CS4125_Project.model.Register import *
# from Movie import Movie
from model.Register import validatePasswordStrength, emailValidator, ensurePasswordsAreEqual,\
    registerNewUser, checkIfEmailExists

from model.SignIn import verifyEmailAndPassword, checkEmailExists, signInUser

from model.Movie import MovieFactory

movieFactory = MovieFactory.MovieFactory()

from model.Admin.AddMovie import addNewReleaseMovie, addChildrensMovie, addStandardMovie, addMovieToCSV

from model.Basket.Stripe_Basket import * #NEW#

TEMPLATES_PATH_STRING = str(os.path.abspath('..')) + '/templates'
STATIC_PATH_STRING = str(os.path.abspath('..')) + '/static'
MOVIE_CSV_PATH_STRING = str(os.path.abspath('..')) + '/csv_files/movies.csv'

app = Flask(__name__,
            template_folder=TEMPLATES_PATH_STRING,
            static_folder=STATIC_PATH_STRING
            )
app.secret_key = 'secret key ahh'

##Getting necessary stripe api keys from .env file
stripe_keys = {
    "secret_key": config("SECRET_KEY"),
    "publishable_key": config("PUBLISHABLE_KEY"),
    "endpoint_key": config("ENDPOINT_SECRET")
}#NEW#

stripe.api_key = stripe_keys["secret_key"]

def __init__(self, name):
    self.app = Flask(name)


# reading the data in the csv file

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/config")
def get_publishable_key():
    stripe_config = {"publicKey": stripe_keys["publishable_key"]}
    return jsonify(stripe_config)

@app.route('/movies')
def movie():
    
        df = pd.read_csv(MOVIE_CSV_PATH_STRING, usecols=['TITLE','TICKETS'])
        movieNameAndTicket = df.set_index('TITLE')['TICKETS'].to_dict()
        return render_template('Movie.html',  movieNameAndTicket = movieNameAndTicket)

@app.route('/')
def home():
    return render_template('home.html')

# @app.route("/test", methods=['POST'])
# def buy_ticket_for_movie():
#
#     df = pandas.read_csv(CSV_PATH_STRING)
#     movieName = df['MOVIE'].tolist()
#
#     # Check which button was clicked on the movies page by reading the request form and getting the movie name from that
#     # Finding the column index of the movie in the CSV file
#     index = movieName.index(list(request.form.to_dict())[0])
#
#     # Decrease the ticket amount when a ticket is bought and update the CSV file
#     df.at[index, 'TICKETS'] = df.at[index, 'TICKETS'] - 1
#     df.to_csv(CSV_PATH_STRING, index=False)
#
#     return redirect('/movies')


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
    return render_template('base.html', data=session['signin'])

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

@app.route("/create-checkout-session")
def create_checkout_session():
    domain_url = "http://127.0.0.1:5000/"
    stripe.api_key = stripe_keys["secret_key"]
    line_items = []    ##NEEDS UPDATE
    try:
        checkout_session = stripe.checkout.Session.create(
            success_url=domain_url + "success?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=domain_url + "cancelled",
            payment_method_types=["card"],
            mode="payment",
            line_items = bask.getBasket() ##NEEDS UPDATE
        )
        return jsonify({"sessionId": checkout_session["id"]})
    except Exception as e:
        print(line_items)
        return jsonify(error=str(e)), 403

##Creating a webhook for realtime updates/ Maybe not necessary for our app?? 
@app.route("/webhook", methods=["POST"])
def stripe_webhook():
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get("Stripe-Signature")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, stripe_keys["endpoint_secret"]
        )

    except ValueError as e:
        # Invalid payload
        return "Invalid payload", 400
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return "Invalid signature", 400

    # Handle the checkout.session.completed event
    if event["type"] == "checkout.session.completed":
        print("Payment was successful.")

    return "Success", 200