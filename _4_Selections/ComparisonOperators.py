#  <   less than                         radius < 0 False
#  <=  less than or equal to             radius <= 0 False
#  >   greater than radius > 0           True
#  >=  greater or equal to radius >= 0   True
#  ==  equal to radius == 0              False
#  !=  not equal to radius != 0          True

radius = 5

print(radius > 0)
print(radius < 0)

# Internally, Python uses 1 to represent True and 0 for False.
# You can use the int function to convert a Boolean value to an integer.
# Boolean values always returns false when value is 0.

print(int(True))
print(int(False))

print(bool(0))
print(bool(1))
print(bool(-1))
print(bool(4))
