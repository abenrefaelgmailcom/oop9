# Exercise – Point Class
# Create a class named Point that represents a 2D point with coordinates x and y
#
# Requirements:
# In the constructor (__init__), receive the values x and y, and store them as private attributes
#
# Write getter and setter methods for both attributes
#
# Fully implement:
#
# __repr__
# __str__
# __eq__
# __hash__
# Create two points with the same values (e.g., Point(3, 4) and Point(3, 4))
#
# Store a value in a dictionary using the first object as a key (e.g., value should be the result of sqrt(x^2 + y^2))
#
# Add another value using the second object as a key (e.g., a string or a label of your choice)
#
# Print the dictionary
#
# Thinking Questions:
# How many items are actually stored in the dictionary and why?
#
# What is a hash collision? and can it happen here?
#
# What is reference count in memory and how is it related to GC (garbage collection)?



from math import sqrt

class Point:
    def __init__(self, x, y):
        # privet fields
        self.__x = x
        self.__y = y

    # Getter ־x
    def get_x(self):
        return self.__x

    # Setter ־x
    def set_x(self, value):
        self.__x = value

    # Getter ־y
    def get_y(self):
        return self.__y

    # Setter ־y
    def set_y(self, value):
        self.__y = value

    # regular print
    def __str__(self):
        return f"Point({self.__x}, {self.__y})"

    #  for devs/debug
    def __repr__(self):
        return f"Point({self.__x}, {self.__y})"

    # compare two objects by values
    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.__x == other.__x and self.__y == other.__y

    #  hash value for dictionary use or set
    def __hash__(self):
        return hash((self.__x, self.__y))


# create two points with the same values
p1 = Point(3, 4)
p2 = Point(3, 4)

# create dictionary
points_dict = {}

# add value by p1
points_dict[p1] = sqrt(3**2 + 4**2)  # תוצאה: 5.0

# add value by p2 (suppost to change)
points_dict[p2] = "point on label"

# print dictionary
print(points_dict)



