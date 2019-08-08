class ModeOfTransportation:

    def move(self):
        print('i can move')


# inheritance - subclass from a parent class
class Car(ModeOfTransportation):

    # initialize the properties of the class
    def __init__(self, brand, color, model, price):
        self.brand = brand
        self.color = color
        self.type = model
        self.price = price


class Bike(ModeOfTransportation):
    def __init__(self, brand, color, model, price):
        self.brand = brand
        self.color = color
        self.type = model
        self.price = price


toyota = Car(brand='Toyota', color='Black', model='Sedan', price=100000000)
honda = Car(brand='Honda', color='White', model='City Car', price=200000000)
toyota.move()
honda.move()
print(type(honda))

print('The color of Toyota is', toyota.color)