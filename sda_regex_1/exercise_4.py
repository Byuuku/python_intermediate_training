import re


def exercise_4():
    print("Enter text including 'ala' string")

    value = input()

    expression = r".*ala.*"

    if re.fullmatch(expression, value):
        print("Name correct - 'ala' found in text")
    else:
        print("There is no 'ala' inside entered text...")
