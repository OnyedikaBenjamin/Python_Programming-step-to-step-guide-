import math


class Circle:  # Class

    """ Here we created a constructor that allows us to create instance of the class and then
    NOTE : 'Self' must be the first parameter of all methods created in python"""

    def __init__(self, radius):  # Constructor
        self.radius = radius

    def set_radius(self, radius):  # Method to mutate the radius
        self.radius = radius

    def get_radius(self):  # Method to access the radius
        return self.radius

    def get_perimeter(self):  # Method to compute the perimeter
        return 2 * self.radius * math.pi

    def get_area(self):  # Method to compute the area
        return self.radius * self.radius * math.pi


circle1 = Circle(0)
circle2 = Circle(0)

circle1.set_radius(5)  # First object reference
circle2.set_radius(4)  # Second object reference

print(circle1.get_radius())
print(circle2.get_radius())

print("Circle 1 area is", format(circle1.get_area(), ".2f"),
      "and its perimeter is", format(circle1.get_perimeter(), ".2f"))
print("Circle 2 area is", format(circle2.get_area(), ".2f"),
      "and its perimeter is", format(circle2.get_perimeter(), ".2f"))
