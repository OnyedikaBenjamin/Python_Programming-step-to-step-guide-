#  Write a program that randomly generates an integer between 0 and 100, inclusive. The program prompts the user to
#  enter numbers continuously until it matches the randomly generated number. For each user
#  input, the program reports whether it is too low or too high, so the user can choose the next
#  input intelligently.
import random

number = random.randint(0, 100)
userAnswer = -1

while userAnswer != number:
    userAnswer = eval(input("Guess The Number : "))
    if userAnswer > number:
        print("Number is too high!")
    elif userAnswer < number:
        print("your guess is too low!")

if userAnswer == number:
    print("You are correct!")
