""" # Create a program randomly generates a
lottery of a two-digit number, prompts the user to enter a two-digit number, and determines
whether the user wins according to the following rules:
1. If the user input matches the lottery number in the exact order, the award is $10,000.
2. If all digits in the user input match all digits in the lottery number, the award is $3,000.
3. If one digit in the user input matches a digit in the lottery number, the award is $1,000.
Note that the digits of a two-digit number may be 0. If a number is less than 10, we assume
the number is preceded by a 0 to form a two-digit number. For example, number 8 is treated
as 08 and number 0 is treated as 00 in the program. """
import random

number = random.randint(10, 99)
print(number)

firstDigit = number // 10
secondDigit = number % 10

userInput = eval(input("Enter a two digit number : "))

userFirstDigit = userInput // 10
userSecondDigit = userInput % 10

if userInput == number:
    print("Exact match : You've won $10,000")
elif userFirstDigit == secondDigit and userSecondDigit == firstDigit:
    print("Match all digit : You've won $3000")
elif userFirstDigit == firstDigit\
        or userFirstDigit == secondDigit\
        or userSecondDigit == firstDigit\
        or userSecondDigit == secondDigit:
    print("Match one digit : You've won $1000")
else:
    print("Sorry no match")
