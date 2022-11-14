import BasketState
import BasketEmpty

class ItemsInBasket(BasketState):
   
    def addItems(self, item, quantity) -> None:
        pass

    def removeItems(self, item, quantity) -> None:
        pass
        ##if items reduced to 0 basket is empty

    def clearBasket(self) -> None:
        print("Removing all items from basket")
        self.order.setOrderState(BasketEmpty())