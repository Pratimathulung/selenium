# Create a class Fruit. Define 3 methods in this class __init__(), nutrition(), fruit_shape(). Print anything you like
# in these methods.
# Create one more class(Any fruit name)
# This class should inherit from the Fruit class created above, this will become the child class and 'Fruit' will be
# referred as parent class to this class
# Define 3 methods in this class __init__(), nutrition(), color(). Print anything you like in these methods.
# Create instances from these classes and call methods from them. Call methods from the base class also using the
# instance of the child class

class Fruit:
    def __init__(self):
        print('Fruits are healthy')

    def nutrition(self):
        print('Fruits are full of vitamins')

    def fruit_shape(self):
        print('Fruits can be of different shapes')


class Orange(Fruit):
    def __init__(self):
        Fruit.__init__(self)
        print('I am Orange')

    def nutrition(self):
        print('I am full of vitamin C')

    def color(self):
        print('I keep it simple, the color is also orange :)')


f = Fruit()
f.nutrition()
f.fruit_shape()

o = Orange()
o.nutrition()
o.fruit_shape()
o.color()

#
# class Student(Person):
#     def __init__(self, firstName, lastName, idNumber, scores):
#         Person.__init__(self, firstName, lastName, idNumber)
#         self.scores = scores
#
#     def calculate(self):
#         sum = 0
#         for score in scores:
#             sum += score
#         average = sum / len(scores)
#         if average < 40:
#             return "T"
#         elif (average >= 40) and (average < 55):
#             return "D"
#         elif (average >= 55) and (average < 70):
#             return "P"
#         elif (average >= 70) and (average < 80):
#             return "A"
#         elif (average >= 80) and (average < 90):
#             return "E"
#         else:
#             return "O"
