# We can swap the values of variables using the syntax 'x, y = y, x'

number1 = 2
number2 = 5
print("Before the swap, number1 is", number1, "and number2 is", number2)
number1, number2 = number2, number1   # Swap the elements of the variables
print("After the swap, number1 is", number1, "and number2 is", number2)
x = 1
y = 2
temp = x    # Save x in a temp variable
x = y      # Assign the value in y to x
y = temp   # Assign the value in temp to y



