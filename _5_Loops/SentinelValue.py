data = 1
number = 0
sumOfNumbers = 0

while data != 0:
    userInput = eval(input("Enter number : "))
    sumOfNumbers += userInput

    data = eval(input("Enter any number to add more numbers to the Sum "
                      "or enter 0 to quit : "))
print("Sum of the numbers is", sumOfNumbers)

    