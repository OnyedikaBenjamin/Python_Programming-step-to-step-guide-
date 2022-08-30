number1 = eval(input("Enter the first number : "))
number2 = eval(input("Enter the second number : "))
number3 = eval(input("Enter the third number : "))
average = (number1 + number2 + number3) / 3
print("The average of", number1, number2, number3, "is", average)

# The above Statement can also be written in the format below

number1, number2, number3 = eval(input("Enter three numbers seperated by commas : "))
average = (number1 + number2 + number3) / 3
print("The average of", number1, number2, number3, "is", average)
