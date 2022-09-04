# A function is a collection of statements that performs an action.
# Write a function that sum up numbers from a certain range.

def add(number1, number2):
    result = 0
    for x in range(number1, number2 + 1):
        result += x

    return result


def execute():
    print("Sum from 1 to 10 is", add(1, 10))
    print("Sum from 20 to 37 is", add(20, 37))
    print("Sum from 35 to 49 is", add(35, 49))


execute()
