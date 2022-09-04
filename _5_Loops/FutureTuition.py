# Suppose that the tuition for a university is $10,000 this year and increases 7% every year. In
# how many years will the tuition have doubled?

tuition = 10000
doubledTuition = 2 * tuition
year = 0

while tuition < doubledTuition:
    tuition += 0.07 * tuition
    year += 1
print("The tuition will be doubled in ", year, "years time, and it will be $", format(tuition, ".2f"))
