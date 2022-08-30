""" Write a program that obtains minutes and remaining seconds from an amount of time in seconds. """

seconds = eval(input("Enter a value in seconds : "))
minutes = seconds // 60
remainderSeconds = seconds % 60

print(seconds, "seconds", "is", minutes, "minutes and", remainderSeconds, "seconds.")
