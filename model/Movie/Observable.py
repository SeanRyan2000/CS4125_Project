import os
import pandas as pd

USERS_CSV_PATH = str(os.path.abspath('..')) + '/csv_files/users.csv'


class Observable():

    def __init__(self):
        email = pd.read_csv(USERS_CSV_PATH)
        self.userEmail = email['EMAIL'].tolist()

    def unregister(self, user):
        self.userEmail.remove(user.getUserEmail())

    def notify_user(self):
        for email in self.userEmail:
            print("Email sent to: " + email)


