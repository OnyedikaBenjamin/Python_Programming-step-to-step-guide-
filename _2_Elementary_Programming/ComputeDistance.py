# Write a program that prompts the user to enter two points and computes the distance between them.
# Given that the formular for computing distance is = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5

x1, y1 = eval(input("Enter x1 and y1 for point 1 : "))
x2, y2 = eval(input("Enter x2 and y2 for point 2 : "))
distance = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5

print("The distance between the two points is", distance)
