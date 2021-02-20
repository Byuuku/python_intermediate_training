import re


def exercise_1():
    print("Enter your number:")
    value = input()

    expression = "[0-9]+"
    if re.fullmatch(expression, value):
        print("Number found")
        if int(value) % 2 == 0:
            print("-> even number")
        else:
            print("-> odd number")
    else:
        print("Incorrect input, must be number")
