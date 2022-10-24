from User import User
import csv

class Staff(User):
    def __init__(self, email, password, ID_number, isAdmin):
        super().__init__(email, password, ID_number, isAdmin)
    
    ##Method for Staff User Type
    def getUserType(self):
        return "Staff"
    
    