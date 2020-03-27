
class Product:
    
    def __init__(self, name, description, price):
        # properties
        self.name = name
        self.description = description
        self.price = price
    
    def discount_price(self, rate):
        final_price = self.price - (self.price * (rate/100))
        return round(final_price,2)

    # string representation of the object
    def __str__(self):
        return("{0} - {1}".format(self.name, self.price))
    

air_max = Product(name="Nike Air Max", description="The one and only shoes", price=120.99)

print(air_max.discount_price(10))

print(air_max)

class Shoe(Product):
    pass