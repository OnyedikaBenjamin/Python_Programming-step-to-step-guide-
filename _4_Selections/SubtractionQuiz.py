# Generate two single-digit integers for number1 and number2.  If number1 < number2, swap number1 with number2.
# Prompt the student to answer, "what is number1 - number2?"   Check the student’s answer and display whether the answer
# is correct.
import random

number1 = random.randint(0, 100)
number2 = random.randint(0, 100)

if number1 < number2:
    number1, number2 = number2, number1

answer = number1 - number2

userAnswer = eval(input("What is " + str(number1) + " - " + str(number2) + " ? : "))
if userAnswer == answer:
    print("Correct")
else:
    print("Your answer is wrong,", number1, "-", number2, "is", answer)


