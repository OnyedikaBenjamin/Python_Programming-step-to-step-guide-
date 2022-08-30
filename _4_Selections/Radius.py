import math

radius = eval(input("Enter the radius : "))
if radius < 0:
    print("Incorrect input")
else:
    area = radius * radius * math.pi
    print("Area is", area)
