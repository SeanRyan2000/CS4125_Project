import datetime
import time
from abc import ABCMeta, abstractmethod

"Interface"


class iTicket(metaclass=ABCMeta):  # pylint: disable=too-few-public-methods
    "The command interface, that all commands will implement"

    @staticmethod
    @abstractmethod
    def execute():
        "The required execute method that all command objects will use"


"Invoker"


class Invoker:
    "The Invoker Class"

    def __init__(self):
        self._commands = {}
        self._history = []

    def show_history(self):
        "Print the history of each time a command was invoked"
        for row in self._history:
            print(
                f"{(row[0]).strftime('%H:%M:%S')}"
                f" : {row[1]}"
            )

    def register(self, command_name, command):
        "Register commands in the Invoker"
        self._commands[command_name] = command

    def execute(self, command_name):
        "Execute any registered commands"
        if command_name in self._commands.keys():
            self._commands[command_name].execute()
            self._history.append((time.time(), command_name))
        else:
            print(f"Command [{command_name}] not recognised")


"Reciever Classes"


class Ticket:
    def __init__(self, movieName, movieLength, movieType, numberOfTickets, ticketType, price):
        self.movieName = movieName
        self.movieLength = movieLength
        self.movieType = movieType
        self.ticketType = ticketType
        self.price = price
        self.numberOfTickets = numberOfTickets

    ##Print Ticket Information
    def returnTicketInfo(self):
        return "Movie: {}\n Time: {}\n Type: {}\n Ticket: {}\n Price: {}\n".format(self.movieName, self.movieLength,
                                                                                   self.movieType, self.ticketType,
                                                                                   self.price)

    # Get the Price for Ticket
    def getTicketPrice(self):
        price = 0
        if self.movieType == "childrens":
            self.price = self.price * 0.8
        elif self.movieType == "new":
            self.price = self.price * 1.2
        return round(self.price, 2)

    @staticmethod
    def set_kids(TICKETS):
        TICKETS.ticketType = "kids"
        TICKETS.price = 8

    @staticmethod
    def set_students(TICKETS):
        TICKETS.ticketType = "student"
        TICKETS.price = 10

    @staticmethod
    def set_adults(TICKETS):
        TICKETS.ticketType = "adult"
        TICKETS.price = 12

    @staticmethod
    def apply_multiplier(TICKET):
        if TICKET.movieType == "childrens":
            TICKET.price *= 0.8
        elif TICKET.movieType == "new":
            TICKET.price *= 1.2

    @staticmethod
    def multipleTicketPrice(ticket, numberOfTickets):
        ticket.price = ticket.price * numberOfTickets
        return ticket.price


# command interface
class CommandSetKids(iTicket):  # pylint: disable=too-few-public-methods
    """A Command object, that implements the ICommand interface and
    runs the command on the designated receiver"""

    def __init__(self, ticket):
        self._ticket = ticket

    def execute(self):
        self._ticket.set_kids(self._ticket)
        self._ticket.apply_multiplier(self._ticket)


class CommandSetStudent(iTicket):  # pylint: disable=too-few-public-methods
    """A Command object, that implements the ICommand interface and
    runs the command on the designated receiver"""

    def __init__(self, ticket):
        self._ticket = ticket

    def execute(self):
        self._ticket.set_students(self._ticket)
        self._ticket.apply_multiplier(self._ticket)


class CommandSetAdult(iTicket):  # pylint: disable=too-few-public-methods
    """A Command object, that implements the ICommand interface and
    runs the command on the designated receiver"""

    def __init__(self, ticket):
        self._ticket = ticket

    def execute(self):
        self._ticket.set_adults(self._ticket)
        self._ticket.apply_multiplier(self._ticket)


# invoker
# client for test purposes
class main:
    def main():
        # The CLient
        # Create a receiver
        TICKETS = Ticket("Avengers", "2:00", "new", "1", "", 0)
        TICKETS2 = Ticket("Avatar", "6:00", "new", "5", "", 0)
        TICKETS3 = Ticket("Shaw Shank Redemption", "21:00", "old", "7", "", 0)

        COMMAND_KIDS = CommandSetKids(TICKETS)
        COMMAND_STUDENT = CommandSetStudent(TICKETS2)
        COMMAND_ADULT = CommandSetAdult(TICKETS3)

        # Register the commands with the invoker
        INVOKER = Invoker()
        INVOKER.register("1", COMMAND_KIDS)
        INVOKER.register("2", COMMAND_STUDENT)
        INVOKER.register("3", COMMAND_ADULT)

        # Execute the commands that are registered on the Invoker
        INVOKER.execute("1")
        INVOKER.execute("2")
        INVOKER.execute("3")

        print("TICKETS, ticket type = ", TICKETS.ticketType)
        print(TICKETS.returnTicketInfo())

        print("TICKETS2, ticket type = ", TICKETS2.ticketType)
        print(TICKETS2.returnTicketInfo())

        print("TICKETS3, ticket type = ", TICKETS3.ticketType)
        print(TICKETS3.returnTicketInfo())

    main()
