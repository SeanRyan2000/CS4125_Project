from abc import ABC, abstractmethod
import Basket

class BasketState(ABC):

    @property
    def order(self) -> Basket:
        return self._basket

    @order.setter
    def order(self, basket: Basket) -> None:
        self.basket = basket

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


    