import abc
from abc import ABC, abstractmethod
import csv

class User(abc.ABC):
    def __init__(self, email, password, ID_number, isAdmin):
        self.email = email
        self.password = password
        self.ID_number = ID_number
        self.isAdmin = isAdmin


    # TODO LOOK AT WHY THIS IS CAUSING AN ERROR :(
    ##Abstract Method to get user types
    # @abstractmethod
    # def getUserType(self):
    #     pass
    
    ##Return the User Email
    @property
    def getUserEmail(self) -> str:
        return f'Email: {self.email}'
    
    ##Return the User Password
    @property
    def getUserPassword(self) -> str:
        return f'Password: {self.password}'
    
    ##Return the User ID Number
    @property
    def getID_number(self) -> str:
        return f'User ID: {self.ID_number}'
    
    ##Return whether User is an Admin or not
    def getAdminStatus(self) -> str:
        return f'Admin User: {self.isAdmin}'
    
    ##Make a non Admin account an Admin
    def createAdmin(self):
        if self.isAdmin == False:
            self.isAdmin = True
            return f'Admin Account created'
        else:
            return f'Account is already an Admin'