import random

count = 0
correctCount = 0
answer = 0
while count < 5:
    number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)

    if number1 < number2:
        number1, number2 = number2, number1

        answer = number1 - number2

    userInput = eval(input("what is " + str(number1) + " - " + str(number2) + " ? : "))

    if userInput == answer:
        print("You are correct!!!")
        correctCount = correctCount + 1

    else:
        print("You are wrong!")
    count = count + 1

print("You got", correctCount, "Questions correct")


