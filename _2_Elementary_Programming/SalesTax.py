# Write a program that displays the sales tax with two digits after the decimal point
purchaseAmount = eval(input("Enter purchase amount: "))

tax = purchaseAmount * (6/100)
print(tax)
print("Sales tax is", int(tax * 100) / 100)
