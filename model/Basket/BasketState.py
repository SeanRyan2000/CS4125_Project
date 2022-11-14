from abc import ABC, abstractmethod
from Basket import Basket

class BasketState(ABC):

    @property
    def basket(self) -> Basket:
        return self._basket

    @basket.setter
    def basket(self, basket: Basket) -> None:
        self._basket = basket

    @abstractmethod
    def addItem(self, item, quantity) -> None:
        pass

    @abstractmethod
    def removeItem(self, item, quantity) -> None:
        pass

    @abstractmethod
    def updateItem(self) -> None:
        pass

    @abstractmethod
    def clearBasket(self) -> None:
        pass

    @abstractmethod
    def viewBasket(self) -> None:
        pass

    @abstractmethod
    def getTotalCost(self) -> None:
        pass


    