import random

number1 = random.randint(1, 100)
number2 = random.randint(1, 100)
if number1 < number2:
    number1, number2 = number2, number1

correctAnswer = number1 - number2
userAnswer = eval(input("What is " + str(number1) + " - " + str(number2) + " : "))

while userAnswer != correctAnswer:
    userAnswer = eval(input("What is " + str(number1) + " - " + str(number2) + " : "))

    print("You are correct!")



