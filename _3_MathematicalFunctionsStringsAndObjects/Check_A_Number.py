# (Check a number) Write a program that prompts the user to enter an integer and
# checks whether the number is divisible by both 5 and 6, divisible by 5 or 6, or just
# one of them (but not both).

number = eval(input("Please enter your number : "))

divisibleBy5and6 = number % 5 == 0 and number % 6 == 0
divisibleBy5or6 = number % 5 == 0 or number % 6 == 0
divisible_By_5or6_ButNotBoth = not (number % 5 == 6 or number % 6 == 0)

print("Is number divisible by 5 and 6 ?", divisibleBy5and6)
print("Is number divisible by 5 or 6 ?", divisibleBy5or6)
print("Is number divisible by 5 or 6 but not both?", divisible_By_5or6_ButNotBoth)
