import six
from abc import ABCMeta
from Concessions.Popcorn import Popcorn

@six.add_metaclass(ABCMeta)
class AddOns(Popcorn):

    def __init__(self, concession):
        self.concession = concession

    def getDescription(self):
        return self.concession.getDescription()

    def getPrice(self):
        return self.concession.getPrice()
        

class AddDrink(AddOns):
    def __init__(self, concession):
        AddOns.__init__(self, concession)

    def getDescription(self):
        return self.concession.getDescription() + ", Drink"

    def getPrice(self):
        return self.concession.getPrice() + 3


class AddSweets(AddOns):
    def __init__(self, concession):
        AddOns.__init__(self, concession)

    def getDescription(self):
        return self.concession.getDescription() + ", Sweets"

    def getPrice(self):
        return self.concession.getPrice() + 2


class AddIceCream(AddOns):
    def __init__(self, concession):
        AddOns.__init__(self, concession)

    def getDescription(self):
        return self.concession.getDescription() + ", Ice Cream"

    def getPrice(self):
        return self.concession.getPrice() + 4


class AddHotDog(AddOns):
    def __init__(self, concession):
        AddOns.__init__(self, concession)

    def getDescription(self):
        return self.concession.getDescription() + ", Hot Dog"

    def getPrice(self):
        return self.concession.getPrice() + 5