"""   The Chinese Zodiac is based on a twelve-year cycle, with each year represented by an animal—
        monkey, rooster, dog, pig, rat, ox, tiger, rabbit, dragon, snake, horse, or sheep in this roster
 0: monkey
 1: rooster
 2: dog
 3: pig
 4: rat
 5: ox
 6: tiger
 7: rabbit
 8: dragon
 9: snake
 10: horse
 11: sheep
Note that year % 12 determines the Zodiac sign. 1900 is the year of the rat because 1900 % 12 is 4.
Write a program that prompts the user to specify a year, and then it displays the animal for that year.
"""

year = eval(input("Enter a year : "))

if year % 12 == 0:
    print(year, "is the year of the monkey")
elif year % 12 == 1:
    print(year, "is the year of the rooster")
elif year % 12 == 2:
    print(year, "is the year of the dog")
elif year % 12 == 3:
    print(year, "is the year of the pig")
elif year % 12 == 4:
    print(year, "is the year of the rat")
elif year % 12 == 5:
    print(year, "is the year of the ox")
elif year % 12 == 6:
    print(year, "is the year of the tiger")
elif year % 12 == 7:
    print(year, "is the year of the rabbit")
elif year % 12 == 8:
    print(year, "is the year of the dragon")
elif year % 12 == 9:
    print(year, "is the year of the snake")
elif year % 12 == 10:
    print(year, "is the year of the horse")
else:
    print(year, "is the year of the sheep")

