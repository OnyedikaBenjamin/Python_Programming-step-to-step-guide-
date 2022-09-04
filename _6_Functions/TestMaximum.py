# Write a function that takes in two numbers and determine which is the maximum or if they are equal

def maximum(number1, number2):
    if number1 > number2:
        return number1
    elif number2 > number1:
        return number2
    else:
        return "Oh no!, they are Equal"


def execute():
    number1 = eval(input("Enter the first number : "))
    number2 = eval(input("Enter the second number : "))
    print("The maximum of the two numbers is :", maximum(number1, number2))


execute()