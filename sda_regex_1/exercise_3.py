import re


def exercise_3():
    print("Enter your login")

    value = input()

    expression = r"[a-zA-Z0-9_\-]{8,16}"

    if re.fullmatch(expression, value):
        print("This is a correct login!")
    else:
        print("This is incorrect login...")
