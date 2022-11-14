import BasketState
import BasketEmpty

class ItemsInBasket(BasketState):
   
    def addItem(self, item, quantity = 1) -> None:
        if item in self.items:
            self.items[item] += quantity
        else: 
            self.items[item] = quantity

    def removeItem(self, item, quantity = 0) -> None:
        if quantity<=0: 
            self.items.pop(item, None)
        else:
            if item in self.items:
                if quantity<self.items[item]:
                    self.items[item] -= quantity
                else:
                    self.items.pop(item, None)

        if len(self.items) == 0:
            self.order.setOrderState(BasketEmpty())

    def updateItem(self, item, quantity) -> None:
        if quantity > 0: 
            self.items[item] = quantity
        else:
            self.removeItem(item)

    def clearBasket(self) -> None:
        self.items = {}
        self.order.setOrderState(BasketEmpty())

    def viewBasket(self) -> None:
        pass

    def getTotalCost(self) -> None:
        totalCost = 0
        
        for item in self.items:
            quantity = self.items[item]
            cost = quantity * item.price
            totalCost += cost
        
        return totalCost