#  Write  program that prompts the user to enter two positive integers and finds their greatest common divisor.

number1 = eval(input("Enter the first number : "))
number2 = eval(input("Enter the second number : "))

gcd = 1
k = 1

while k < number1 and k < number2:
    if number1 % k == 0 and number2 % k == 0:
        gcd = k
    k += 1
print("The greatest common divisor is ", gcd)
