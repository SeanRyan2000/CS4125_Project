import BasketState
import ItemsInBasket

class BasketEmpty(BasketState):

    def addItems(self, item, quantity) -> None:
        print("Adding item to basket")
        self.order.setOrderState(ItemsInBasket())

    def removeItems(self, item, quantity) -> None:
        print("Cannot remove item, basket is empty")
    
    def clearBasket(self) -> None:
        print("Cannot clear basket, basket is empty")