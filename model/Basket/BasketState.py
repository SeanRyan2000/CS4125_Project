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
    def addItems(self, item, quantity) -> None:
        pass

    @abstractmethod
    def removeItems(self, item, quantity) -> None:
        pass

    @abstractmethod
    def clearBasket(self) -> None:
        pass