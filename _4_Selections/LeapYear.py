# A leap year is divisible by 4 but not by 100 or divisible by 400
# Write a program that lets the user enter a year and then determines whether it is a leap year.

year = eval(input('Enter a year : '))

isLeapYear = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
print("is", year, "a leap year? : ", isLeapYear)



