import os

import pandas
import uuid
import bcrypt

from password_strength import PasswordPolicy
from email_validator import validate_email, EmailNotValidError
import csv
import cryptography

CSV_PATH_STRING = str(os.path.abspath('..')) + '/csv_files/users.csv'

def validatePasswordStrength(pwd):

        policy = PasswordPolicy.from_names(
        length=8,  # min length: 8
        uppercase=1,  # need min. 2 uppercase letters
        numbers=2,  # need min. 2 digits
        special=1,  # need min. 2 special characters
      )

        return len(policy.test(pwd))==0

def ensurePasswordsAreEqual(psw, repeat_psw):

    return psw == repeat_psw

def emailValidator(email):

    try:
        # Check that the email address is valid.
        validation = validate_email(email)

        email = validation.email

    except EmailNotValidError:
        # if email is not valid then it returns false
        return False

    return True

def registerNewUser(email, password):
    password = password.encode('utf-8')
    #hashing password using bcrypt
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
    # Column names in User CSV file
    field_names = ['USER_ID', 'EMAIL', 'PASSWORD']

    # Taking the first 5 digits of a random UUID and adding it to the CSV file for that user
    dict = {"USER_ID": str(uuid.uuid1())[0:5], "EMAIL": email, 'PASSWORD': hashed_password}

    # Writing to the CSV file with the values in the dictionary
    with open('../csv_files/users.csv', 'a') as csv_file:
        dict_object = csv.DictWriter(csv_file, fieldnames=field_names)

        dict_object.writerow(dict)

def checkIfEmailExists(email):

    df = pandas.read_csv(CSV_PATH_STRING)

    # returns true if email already exists in CSV file and false if it doesn't exist
    return email in df['EMAIL'].values


