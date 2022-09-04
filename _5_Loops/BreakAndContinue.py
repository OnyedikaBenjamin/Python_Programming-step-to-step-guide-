# You can use 'continue keyword in a loop. When it is encountered, it ends the current iteration and program
# control goes to the end of the loop body. In other words, continue breaks out of an iteration, while the break
# keyword breaks out of a loop.

sumOfNumbers = 0
number = 0

while number < 100:
    sumOfNumbers += number
    if sumOfNumbers >= 100:
        break
    number += 1
print("All the numbers from 1 to", number, "were summed up \nSum of numbers is", sumOfNumbers)


aNumber = 0
sums = 0

while aNumber < 20:
    aNumber += 1
    if aNumber == 10 or aNumber == 11:  # Don't sum up 10 and 11
        continue
    sums += aNumber
print()
print("All the numbers from 1 to", aNumber, "were summed up excluding 10 and 11\nSum of numbers is", sums)




