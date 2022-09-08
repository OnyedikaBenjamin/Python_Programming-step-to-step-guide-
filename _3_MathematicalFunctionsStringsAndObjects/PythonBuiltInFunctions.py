# abs(x)               Returns the absolute value for x. abs(-2) is 2
# max(x1, x2, ...)     Returns the largest among x1, x2, ... max(1, 5, 2) is 5
# min(x1, x2, ...)     Returns the smallest among x1, x2, ... min(1, 5, 2) is 1
# pow(a, b)            Returns ab. Same as a ** b. pow(2, 3) is 8
# round(x)             Returns an integer nearest to x. If x is equally close to two integers, the even one is returned.
# round(5.4)           is 5
# round(5.5)           is 6
# round(4.5)           is 4
# round(x, n)         Returns the float value rounded to n digits after the decimal point (to n decimal place).
# round(5.466, 2)     is 5.47
# round(5.463, 2)     is 5.46
# fabs(x)             Returns the absolute value for x as a float. fabs(-2) is 2.0
# ceil(x)             Rounds x up to its nearest integer and returns that integer. ceil(2.1) is 3
# ceil(-2.1)          is -2
# floor(x)            Rounds x down to its nearest integer and returns that integer. floor(2.1) is 2
# floor(-2.1)         is -3
import math

letter = 'A'  # Same as letter = "A"
numChar = '4'  # Same as numChar = "4"
message = "Good morning"  # Same as message = 'Good morning'

# Python Escape Sequences

#  \b   Backspace
#  \t   Tab
#  \n   Linefeed
#  \f   Form feed
#  \r   Carriage Return
#  \\   Backslash
#  \'   Single Quote
#  \"   Double Quote
print("He said \"John's program is easy to read\"")
print("Hello World \nPython is getting Interesting")

# The end function allows concatenation of another print line
radius = 3
print("The area is", radius * radius * math.pi, end=' ')
print("and the perimeter is", 2 * radius)

# The str function can be used to convert a number into a string. For example,
x = str(3.4)  # Convert a float to a string
print(x)
y = str(3)  # Convert an integer to a string
print(y)

#  The + operator can be used to concatenate two strings. For example,
message = " Welcome" + " To " + "Python "
print(message)
print(message + "and python is fun")
chapterNumber = 3
print("Chapter " + str(chapterNumber))

# We can use the 'type' to get the data type info of an object
noOfBalls = 6
name = "Ben"
height = 6.7
print(type(name))        # String
print(type(noOfBalls))  # Int
print(type(height))    # Float
