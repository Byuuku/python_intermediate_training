import re


def exercise_2():
    print("Enter postal code number:")
    value = input()

    expression = "[0-9]{2}-[0-9]{3}"
    if re.fullmatch(expression, value):
        print("Postal code number is correct")
    else:
        print("Incorrect postal code number")
