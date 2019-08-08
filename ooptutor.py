class ModeOfTransportation:
    def move(self):
        print('i can move people', type(self))


class Car(ModeOfTransportation):

    wheels = 4

    def forward(self):
        print('i can move forward with my four wheels', type(self))


class Bike(ModeOfTransportation):

    wheels = 2

    def __init__(self, brand, type):
        self.brand = brand
        self.type = type

    def pedaling(self):
        print('moving forward by pedaling')

    def description(self):
        print('I\'m a {0} and brand {1}'.format(self.type, self.brand))

#bmw = Car()

#bmw.forward()

brompton = Bike(brand='brompton', type='folding bike')

#print(brompton.wheels)
print(brompton.description())


