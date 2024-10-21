'''
Write code that will be used by a Shopping cart service to enforce rules on the order

eg. Offer free 2 day shipping on orders > $35 if customer is not a prime member 
Offer free 2 day shipping on all orders if customer is a prime member 
Offer free 1 day shipping for order that are > $125
Offer free 2 hour shipping for prime customer that have > $25 and the items are grocery items

Make this extensible to add other rules in the future Apply a 10% discount if an item has been marked for subscribe and save

I was thinking of creating a Shopping cart class and create one prime member class and other non prime member.
interfaces for Shipping speed calculator and one for discount calculator
What should be best design for this
'''

class Cart():
    def __init__(self, customer_type, items: [Item]):
        self.customer_type = customer_type
        self.category = category
        
    def getShippingCarges(self):
        pass

class Shipping():
    def __init__(self, customer_type, item: Item):
        self.customer_type = customer_type
        self.item = item
    
    def getCharges(self):
        item_traits = self.item.getTraits()
        item_type = item_traits['type']
        item_price = item_traits['price']
        
        charges = None
        time = 0
        rules = {
            'prime': {
                'grocery': {
                    25: 120,    
                },
                'other': {
                    125: 24 * 1 * 60,
                },
                'default': 24 * 2 * 60
            },
            'other': {
                35: 24 * 2 * 60,
            }
        }
        
        if self.customer_type in rules:
            items_dict = rules[self.customer_type]
            if item_type in items_dict:
                price_dict = items_dict[item_type]
            else:
                price_dict = items_dict['other']
        else:
            price_dict = rules['other']
        
        for price in price_dict:
            if item_price > price:
                charges = 0
                time = price_dict[price]
        
        return [charges, time]
             
        
class Item():
    def __init__(self, item_type, price, quantity, coupon, subscribed):
        self.type = item_type
        self.price = price
        self.quantity = quantity
        self.coupon = coupon
        self.subscribed = subscribed
    
    def getTraits(self):
        return {
            'type': self.type,
            'price': self.price,
            'quantity': self.quantity,
            'coupon': self.coupon
        }
    
    def getDiscount(self):
        discount_percent = 0
        if self.subscribed:
            discount_percent = 10
        
        return self.price * (discount_percent / 100)

    def totalPrice(self):
        discount = self.getDiscount()
        return self.price - discount
    