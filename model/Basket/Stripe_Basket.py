product_catalogue = {
    'NEW-ADULT' : 1440,
    'NEW-STUDENT' : 1200,
    'NEW-KIDS' : 960,
    'CHILDRENS-ADULT' : 960,
    'CHILDRENS-STUDENT' : 800,
    'CHILDRENS-CHILD' : 640,
    'ADULT' : 1200,
    'STUDENT' : 1000,
    'CHILD' : 800,
    'HOTDOG' : 500,
    'ICECREAM' : 400,
    'SWEETS' : 200,
    'DRINK' : 300,
    'REGULAR-POPCORN' : 600,
    'LARGE-POPCORN' : 800
}

class LineItem:  
    def __init__(self, price_data, quantity):
        self.price_data = price_data
        self.quantity = quantity
        
    def setLineItem(self, currency, unit_amount, name, quantity):
        self.currency = currency
        self.unit_amount = unit_amount
        self.name = name
        self.quantity = quantity


class Stripe_Basket:
    def __init__(self, line_items):
        self.line_items = line_items

    ##Needs to take in the product name to work, Needs to make Dict
    def addToStripe(self, lineItem, quantity): 
        newItem = LineItem(0, 0)
        newItem.setLineItem('eur', product_catalogue[lineItem], lineItem, quantity)
        self.line_items.append({'price_data':{
                    'currency': newItem.currency,
                    'unit_amount': newItem.unit_amount,
                    'product_data': {
                        'name': newItem.name
                    }
                },
                'quantity': newItem.quantity})
        
    def removeFromStripe(self, name):
        for obj in self.line_items:
            if obj.price_data[2] == name:
                self.line_items.remove(obj)
                break
        print("Item removed from Basket")
        
    def getBasket(self):
        return self.line_items