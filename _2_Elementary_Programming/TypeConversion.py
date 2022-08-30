number = 25.79
numbers = "60.88"

print(int(number))           # This ignores the fractional part of the number
print(round(number))        # This rounds the number to the nearest whole number
print(int(eval(numbers)))  # This converts the string to a floating point value and then cast it to an int

