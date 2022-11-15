import time
from datetime import datetime, date   
from abc import ABCMeta, abstractmethod

"""Reciever Class"""
class Ticket:
    def __init__(self, movie, ticketType):
        self.movieName = movie.getMovieName()
        self.movieLength = movie.getMovieLength()
        self.movieType = movie.getMovieType()
        self.ticketType = ticketType
    
    ##Get the Price for Ticket
    def getPrice(self):
        return self.price

    def getMovieInfo(self) -> str:
        return "{} ({})".format(self.movieName, self.movieLength)

    @staticmethod
    def set_kids(TICKET):
        TICKET.ticketType = "kids"
        TICKET.price = 8

    @staticmethod
    def set_student(TICKET):
        TICKET.ticketType = "student"
        TICKET.price = 10

    @staticmethod
    def set_adult(TICKET):
        TICKET.ticketType = "adult"
        TICKET.price = 12

    @staticmethod
    def apply_multiplier(TICKET):
        if TICKET.movieType == "childrens":
            TICKET.price *= 0.8
        elif TICKET.movieType == "new":
            TICKET.price *= 1.2


"""Interface"""
class iTicket(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def execute():
        pass


"""Invoker"""
class Invoker:
    def __init__(self):
        self._commands = {}
        self._history = []

    def show_history(self):
        for row in self._history:
            print(
                f"{(row[0]).strftime('%H:%M:%S:')}"
                f" : {row[1]}"
            )

    def register(self, command_name, command):
        self._commands[command_name] = command

    def execute(self, command_name):
        if command_name in self._commands.keys():
            self._commands[command_name].execute()
            self._history.append((datetime.now( ), command_name))
        else:
            print(f"Command [{command_name}] not recognised")

    def replay_last(self, number_of_commands):
        commands = self._history[-number_of_commands:]
        for command in commands:
            self._commands[command[1].execute()]


"""
COMMAND SETS
"""
class CommandSetKids(iTicket):
    def __init__(self, ticket):
        self._ticket = ticket

    def execute(self):
        self._ticket.set_kids(self._ticket)
        self._ticket.apply_multiplier(self._ticket)

class CommandSetStudent(iTicket):
    def __init__(self, ticket):
        self._ticket = ticket

    def execute(self):
        self._ticket.set_student(self._ticket)
        self._ticket.apply_multiplier(self._ticket)

class CommandSetAdult(iTicket):
    def __init__(self, ticket):
        self._ticket = ticket

    def execute(self):
        self._ticket.set_adult(self._ticket)
        self._ticket.apply_multiplier(self._ticket)
