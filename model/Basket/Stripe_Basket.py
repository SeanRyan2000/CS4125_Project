
product_catalogue = {
    'NEW-MOVIE-ADULT' : 1440,
    'NEW-MOVIE-STUDENT' : 1200,
    'NEW-MOVIE-KIDS' : 960,
    'KIDS-MOVIE-ADULT' : 960,
    'KIDS-MOVIE-STUDENT' : 800,
    'KIDS-MOVIE-KIDS' : 640,
    'ADULT-TICKET' : 1200,
    'STUDENT-TICKET' : 1000,
    'KIDS-TICKET' : 800,
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
            if obj.name == name:
                self.line_items.remove(obj)
                break
        
        
    def getBasket(self):
        return self.line_items
    
