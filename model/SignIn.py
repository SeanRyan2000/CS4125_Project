import os

import pandas
from flask import request

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
    password = password.encode('utf-8')
    pwd = df.at[index, 'PASSWORD']
    #checking encrypted password in CSV against entered password
    if bcrypt.checkpw(password, pwd.encode('utf-8')):
        return True
    else:
        return False




