def sortBySize(number1, number2):
    if number1 < number2:
        return number1, number2
    else:
        return number2, number1


n1, n2 = sortBySize(567, 43)
print("n1 is", n1, "\nn2 is", n2)
