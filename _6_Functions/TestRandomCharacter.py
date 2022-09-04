# Here we will generate 100 lower case letters and display them 20 per line

import RandomCharacter

numberOfLettersToBeGenerated = 100
lettersToBePrintedPerLine = 20

for i in range(numberOfLettersToBeGenerated):
    print(RandomCharacter.generateRandomLowerCaseLetter(), end="")
    if (i + 1) % lettersToBePrintedPerLine == 0:                    # If it prints up to 10
        print()                                                     # Jump to next line

