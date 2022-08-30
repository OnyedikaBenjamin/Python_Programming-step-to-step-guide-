name = " Ben Billion "
hint = "  Welcome"
print(name.lower())              # prints name in lower case letters
print(name.upper())              # prints name in upper case letters
print((hint + name).strip())     # removes the white spaces on both ends of a string

# We can use the format function to specify how many floating point values we need after the decimal point
amount = 12618.98
interestRate = 0.0013
interest = amount * interestRate
print("Interest is", format(interest, ".2f"))
