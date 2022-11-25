import unittest
import six
from abc import ABCMeta
from Popcorn import LargePopcorn, Popcorn

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
        return self.concession.getDescription() + " + Drink"

    def getPrice(self):
        return self.concession.getPrice() + 3


class AddSweets(AddOns):
    def __init__(self, concession):
        AddOns.__init__(self, concession)

    def getDescription(self):
        return self.concession.getDescription() + " + Sweets"

    def getPrice(self):
        return self.concession.getPrice() + 2


class AddIceCream(AddOns):
    def __init__(self, concession):
        AddOns.__init__(self, concession)

    def getDescription(self):
        return self.concession.getDescription() + " + Ice Cream"

    def getPrice(self):
        return self.concession.getPrice() + 4


class AddHotDog(AddOns):
    def __init__(self, concession):
        AddOns.__init__(self, concession)

    def getDescription(self):
        return self.concession.getDescription() + " + Hot Dog"

    def getPrice(self):
        return self.concession.getPrice() + 5

# add a hot dog to a large popcorn
class testAddHotDogToLargePopcorn(unittest.TestCase):
    def testAddHotDogToLargePopcorn(self):
        largePopcorn = LargePopcorn()
        largePopcorn = AddHotDog(largePopcorn)
        self.assertEqual(largePopcorn.getDescription(), "Large Popcorn + Hot Dog")
        print(largePopcorn.getPrice())
        print(self.assertEqual(largePopcorn.getPrice(), 13))
testAddHotDogToLargePopcorn().testAddHotDogToLargePopcorn()

