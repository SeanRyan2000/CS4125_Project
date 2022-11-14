from abc import ABC, abstractmethod
from __future__ import annotations
import BasketState

class Basket:
    _basketState = None

    def __init__(self, state: BasketState) -> None:
        self.setBasketState(state)
        self.items = {}

    
    def setOrderState(self, state: BasketState):
        self._basketState = state
        self._basketState.basket = self

    def presentState(self):
        print(f"Basket is {type(self._basketState.__name__)}")

    def addItems(self, item, quantity):
        self._basketState.addItem(item, quantity)

    def removeItems(self, item, quantity):
        self._basketState.removeItem()

    def clearBasket(self):
        self._basketState.clearBasket()