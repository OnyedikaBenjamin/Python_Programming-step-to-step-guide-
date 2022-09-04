# Write a program that takes in a score and grade it

def grade(score):
    if score > 80:
        print("A")
    elif score > 70:
        print("B")
    elif score > 60:
        print("C")
    else:
        print("Failed")


def execute():
    score = eval(input("Enter a score : "))
    grade(score)


execute()
