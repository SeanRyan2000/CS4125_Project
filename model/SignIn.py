import os

import pandas
from flask import request

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

    return password == pwd




