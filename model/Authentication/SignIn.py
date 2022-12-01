import os

import pandas
from flask import session
from model.User import Customer
import bcrypt

CSV_PATH_STRING = str(os.path.abspath('..')) + '/csv_files/users.csv'


def checkEmailExists(email):
    df = pandas.read_csv(CSV_PATH_STRING)

    # returns true if email already exists in CSV file and false if it doesn't exist
    return email in df['EMAIL'].values


def verifyEmailAndPassword(email, password):

    df = pandas.read_csv(CSV_PATH_STRING)
    eMail = df['EMAIL'].tolist()
    index = eMail.index(email)
    pwd = df.at[index, 'PASSWORD']
    # checking encrypted password in CSV against entered password
    if bcrypt.checkpw(password.encode('utf-8'), pwd.encode('utf-8')):
        signInUser(email)
        return True
    else:
        return False


def getUserID(email):

    df = pandas.read_csv(CSV_PATH_STRING)
    eMail = df['EMAIL'].tolist()
    index = eMail.index(email)
    return df.at[index, 'USER_ID']


def signInUser(email):

    current_user = Customer.User(getUserID(email), email, False)
    session['user'] = current_user.__dict__
    return current_user
