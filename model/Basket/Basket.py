from __future__ import annotations
from abc import ABC, abstractmethod

"""
Basket Context Class
"""
class Basket:
    _basketState = None

    def __init__(self, basketState: BasketState) -> None:
        self.setBasket(basketState)
        self._items = {}
        self._commands = {}
        self._history = []

    ##State Methods
    def setBasket(self, basketState: BasketState):
        self._basketState = basketState
        self._basketState.basket = self

    ##Basket Methods
    def addItem(self, item, quantity = 1):
        self._basketState.addItem(item, quantity)

    def removeItem(self, item, quantity = 0):
        self._basketState.removeItem(item, quantity)

    def updateItem(self, item, quantity):
        self._basketState.updateItem(item, quantity)

    def clearBasket(self):
        self._basketState.clearBasket()

    def viewBasket(self):
        self._basketState.viewBasket()

    def getTotalCost(self):
        self._basketState.getTotalCost()


"""
Abstract Basket State Class
"""
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
    def updateItem(self, item, quantity) -> None:
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


"""
Concrete Basket Empty Class
"""
class BasketEmpty(BasketState):

    def addItem(self, item, quantity = 1) -> None:
        self.basket._items[item] = quantity
        self.basket.setBasket(ItemsInBasket())

    def removeItem(self, item, quantity) -> None:
        print("Cannot remove item, basket is empty")
    
    def updateItem(self, item, quantity) -> None:
        print("No items in basket to update")
  
    def clearBasket(self) -> None:
        print("Cannot clear basket, basket is empty")

    def viewBasket(self) -> None:
        print("There are no items in your basket")

    def getTotalCost(self) -> None:
        print("There are no items in your basket")


"""
Concrete Items in Basket Class
"""
class ItemsInBasket(BasketState):
   
    def addItem(self, item, quantity = 1) -> None:
        if item in self.basket._items:
            self.basket._items[item] += quantity
        else: 
            self.basket._items[item] = quantity

    def removeItem(self, item, quantity = 0) -> None:
        if quantity<=0: 
            self.basket._items.pop(item, None)
        else:
            if item in self.basket._items:
                if quantity<self.basket._items[item]:
                    self.basket._items[item] -= quantity
                else:
                    self.basket._items.pop(item, None)

        if len(self.basket._items) == 0:
            self.basket.setBasket(BasketEmpty())

    def updateItem(self, item, quantity) -> None:
        if quantity > 0: 
            self.basket._items[item] = quantity
        else:
            self.removeItem(item)

    def clearBasket(self) -> None:
        self.basket._items = {}
        self.basket.setBasket(BasketEmpty())

    #Update class to work for Ticket class
    def viewBasket(self) -> None:
        totalCost = 0
        print("---------------------")
        for item in self.basket._items:
            quantity = self.basket._items[item]

            cost = quantity * item.getPrice()
            if hasattr(item, "ticketType"):
                print(" + " + item.getMovieInfo() + " - " + str(quantity) 
                + " x €" + '{0:.2f}'.format(item.getPrice()) 
                + " = €" + '{0:.2f}'.format(cost))
            else:
                print(" + " + item.getDescription() +  " - " + str(quantity)
                + " x €" + '{0:.2f}'.format(item.getPrice())
                + " = €" + '{0:.2f}'.format(cost))
                pass

            totalCost += cost
            
        print("---------------------")  
        print(" = €" + '{0:.2f}'.format(totalCost))
        print("---------------------")

    def getTotalCost(self) -> None:
        totalCost = 0
        
        for item in self.basket._items:
            quantity = self.basket._items[item]
            cost = quantity * item.price
            totalCost += cost
        
        return totalCost