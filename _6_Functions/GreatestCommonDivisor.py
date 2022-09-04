def calculateGCD(number1, number2):
    gcd = 1
    i = 1
    while i < number1 and i < number2:
        if number1 % i == 0 and number2 % i == 0:
            gcd = i
        i += 1
    return gcd