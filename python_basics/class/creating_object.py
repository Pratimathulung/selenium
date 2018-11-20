class Car(object):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        print('Make of the car: ' + self.make)
        print('Model of the car: ' + self.model)


c1 = Car('bmw', '550i')
# print(c1.make)
# print(c1.model)

c2 = Car('benz', 'E350')
# print(c2.make)
c1.info()
c2.info()

