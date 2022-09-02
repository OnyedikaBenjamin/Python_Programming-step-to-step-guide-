# The Syntax for while loop is :

#     i = initialValue  # Initialize loop-control variable
#     while i < endValue:
#
#         .....Loop body.....

#      i += 1   Adjust loop-control variable

i = 0
while i < 6:
    print(i)
    i += 1

# The for loop in Python does not require a counter iteration

# And its syntax is :
#     for i in range(x, y, z):      it will loop from x to y and increment by z
#         print(i)


for i in range(1, 6, 1):
    print("I am a boy")
