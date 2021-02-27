import re


def exercise_7():
    print("Enter your serial number:")

    value = input()

    expression = r"([A-Z0-9!@#\$%\^&\*]{5}-){4}[A-Z0-9!@#\$%\^&\*]{5}"

    if re.fullmatch(expression, value):
        print("Serial number is correct")
    else:
        print("Serial number is incorrect")
