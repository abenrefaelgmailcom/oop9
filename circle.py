
'''
create a Circle class
in the __init__ get the radius (store as private + getter/setter)
add function get_area, __str__, __repr__
implement __eq__
implement __hash__
create 2 circles with the same radius
store in dict a value 'one' using the 1 circle object as key
then store a value 'two' using the 2nd circle object as key
print the dict -- how many items are stored?
'''
import math


class Circle:

    def __init__(self, radius, name):
        self.__radius = radius
        self.__name = name

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value >= 0:
            self.__radius = value

    def get_area(self):
        return math.pi * self.__radius ** 2

    def __repr__(self):
        return f"Circle({self.radius}, '{self.__name}')"

    def __str__(self):
        return f"Circle with radius = {self.radius} area = {self.get_area()} " +\
                    f"name = {self.__name}"

    def __eq__(self, other):
        if isinstance(other, int):
            return self.radius == other
        if not isinstance(other, Circle):
            return False
        return self.radius == other.radius

    def __hash__(self):
        return hash(self.radius)

c1 = Circle(5, 'c1')
c2 = Circle(5, 'c2')
print('c1 == c2', c1 == c2)
print('hash(c1) == hash(c2)', hash(c1) == hash(c2))
print('c1 == 5', c1 == 5)
print('hash(c1) == hash(5)', hash(c1) == 5)
d = dict()
d[c1] = 'one'
d[c2] = 'two'
print("after d[c2] = 'two'", d)
d[5] = 'three'
print("after d[5] = 'three'", d)

d['student'] = 'uri'
h = hash('student')
d[h] = 'uri2'
print(d[h])