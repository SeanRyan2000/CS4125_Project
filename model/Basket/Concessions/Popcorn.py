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

    @abstractmethod
    def getPrice(self) -> None:
        pass


class RegularPopcorn(Popcorn):

    def getDescription(self) -> str:
        return "Regular Popcorn"

    def getPrice(self) -> int:
        return 6


class LargePopcorn(Popcorn):

    def getDescription(self) -> str:
        return "Large Popcorn"

    def getPrice(self) -> int:
        return 8