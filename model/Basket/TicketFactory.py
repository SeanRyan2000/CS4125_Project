

def getTicketPrice(ticket):

    if ticket.ticketType == "Child":
        ticket.price = 8
    elif ticket.ticketType == "Student":
        ticket.price = 10
    elif ticket.ticketType == "Adult":
        ticket.price = 12