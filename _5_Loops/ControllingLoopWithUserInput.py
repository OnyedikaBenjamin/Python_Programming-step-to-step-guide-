import random
import time

answer = 0
continuationCondition = "Y"

while continuationCondition == "Y":

    number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)

    if number1 < number2:
        number1, number2 = number2, number1

    userInput = eval(input("what is " + str(number1) + " - " + str(number2) + " ? : "))

    answer = number1 - number2

    if userInput == answer:
        print("You are correct!!!")
    else:
        print("You are wrong!")

    continuationCondition = input("Enter Y to continue or N to quit : ").upper()
