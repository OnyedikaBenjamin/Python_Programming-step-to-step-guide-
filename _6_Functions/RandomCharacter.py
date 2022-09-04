# Here we create a module named random character with five function that generates specific types of characters
from random import randint


#  To generate a random value, we firstly create a method that generates random values
def generateRandomCharacter(ch1, ch2):
    return chr(randint(ord(ch1), ord(ch2)))


# After then, we can now implement the method to generate different types of random characters
def generateRandomLowerCaseLetter():
    return generateRandomCharacter('a', 'z')


def generateRandomUpperCaseLetter():
    return generateRandomCharacter("F", "X")


def generateRandomDigitCharacter():
    return generateRandomCharacter(0, 9)


# Generate a random character
def generateRandomASCIICharacter():
    return chr(randint(0, 127))
