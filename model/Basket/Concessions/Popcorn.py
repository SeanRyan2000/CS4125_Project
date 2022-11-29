import six
from abc import abstractmethod, ABCMeta

"""
Popcorn:
    Regular ->      6
    Large ->        8

    add Drink:      +3
    add Sweets:     +2
    add IceCream:   +4
    add HotDog:     +5
"""

@six.add_metaclass(ABCMeta)
class Popcorn(object):


    @abstractmethod
    def getDescription(self) -> None:
        pass

    def getQuantity(self) -> int:
        return self.quantity

    @abstractmethod
    def getPrice(self) -> None:
        pass


class RegularPopcorn(Popcorn):

    def __init__(self, quantity):
        self.quantity = quantity

    def getDescription(self) -> str:
        return "Regular Popcorn"

    def getQuantity(self) -> int:
        return self.quantity

    def getPrice(self) -> int:
        return 6 * int(self.quantity)


class LargePopcorn(Popcorn):

    def __init__(self, quantity):
        self.quantity = quantity
    def getDescription(self) -> str:
        return "Large Popcorn"

    def getQuantity(self) -> int:
        return self.quantity

    def getPrice(self) -> int:
        print('QUANTITY: ', self.quantity)
        print('PRICE: ', 8 * self.quantity)
        return 8 * int(self.quantity)