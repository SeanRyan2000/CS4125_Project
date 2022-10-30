from CS4125_Project.model.User import User
import csv

class Customer(User.User):
    def __init__(self, email, password, ID_number, isAdmin):
        super().__init__(email, password, ID_number, isAdmin)
     
     ##Method for Customer User Type  
    def getUserType(self):
        return "Customer"

        