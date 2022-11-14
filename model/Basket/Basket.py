from __future__ import annotations
import BasketState
from Ticket import Ticket

class Basket:
    _basketState = None

    def __init__(self, state: BasketState) -> None:
        self.setBasketState(state)
        self.items = {}

    ##State Methods
    def setOrderState(self, state: BasketState):
        self._basketState = state
        self._basketState.basket = self

    def presentState(self):
        print(f"Basket is {type(self._basketState.__name__)}")

    ##Basket Methods
    def addItem(self, item, quantity = 1):
        self._basketState.addItem(item, quantity)

    def removeItem(self, item, quantity = 0):
        self._basketState.removeItem(item, quantity)

    def updateItem(self):
        self._basketState.updateItem()

    def clearBasket(self):
        self._basketState.clearBasket()

    def viewBasket(self):
        self._basketState.viewBasket()

    def getTotalCost(self):
        self._basketState.getTotalCost()