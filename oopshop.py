class Product:

    def __init__(self, price, name, brand):
        self.price = price
        self.name = name
        self.brand = brand

    def description(self):
        print('the product is {0} and the price is {1}'.format(self.name, self.price))


class Shoes(Product):

    def __init__(self, size, gender):
        self.size = size
        self.gender = gender


class Computer(Product):

    def __init__(self, model, os, price, name, brand):
        super().__init__(price=price, name=name, brand=brand)
        self.model = model
        self.os = os


macbookpro = Computer(price=20000000, name='Mac Book Pro', brand='Apple', os='Mac', model='Laptop')

macbookpro.description()


def buy(product, quantity):
    total = product.price * quantity
    print('total: ', total)


print('you are buying: {0} - {1}'.format(macbookpro.name, macbookpro.brand))
buy(macbookpro, 2)

