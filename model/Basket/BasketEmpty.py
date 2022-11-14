import BasketState
import ItemsInBasket

class BasketEmpty(BasketState):

    def addItem(self, item, quantity = 1) -> None:
        self.items[item] = quantity
        self.order.setOrderState(ItemsInBasket())

    def removeItem(self, item, quantity) -> None:
        print("Cannot remove item, basket is empty")
    
    def updateItem(self, item, quantity) -> None:
        print("No items in basket to update")
  
    def clearBasket(self) -> None:
        print("Cannot clear basket, basket is empty")

    def viewBasket(self) -> None:
        print("There are no items in your basket")

    def getTotal(self) -> None:
        print("There are no items in your basket")