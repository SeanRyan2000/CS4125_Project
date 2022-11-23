from model.User.User import User
import csv

class Customer(User):
    def __init__(self, email, password, ID_number, isAdmin):
        super().__init__(email, password, ID_number, isAdmin)
     
     ##Method for Customer User Type  
    def getUserType(self):
        return "Customer"

    def updateUser(self):

        print(f'Email send to {self.getUserEmail()}. New Movie added.')