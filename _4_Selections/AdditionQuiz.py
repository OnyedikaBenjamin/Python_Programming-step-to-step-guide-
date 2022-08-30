# Write a program to help a first-grader practice addition. The program randomly generates two single-digit integers,
# number1 and number2, displays to the student a question such as What is 1 + 7, After the student types the answer,
# the program displays a message to indicate whether it is true or false.
import random
from random import randint

# We use the randint(x, y) to generate a random number from x to y.
number1 = randint(1, 5)
number2 = randint(6, 10)
answer = number2 + number1

userAnswer = eval(input("What is " + str(number2) + " + " + (str(number1) + " ? : ")))
print(userAnswer == answer)


