def getGrade(score):
    if score > 80:
        return 'A'
    elif score > 70:
        return 'B'
    elif score > 60:
        return 'C'
    else:
        return 'Failed'


def execute():
    score = eval(input("Enter a score : "))
    print(getGrade(score))


execute()
