import sys


def case_1():
    list_of_numbers = [1, 5, 8, 10, 21]
    print("case_1_before")

    # first method
    try:
        result = list_of_numbers[5]
    except IndexError as in_exc:
        print(f"M1 - Index exception: {in_exc.args} caught")
    except Exception as exc:
        print(f"M1 - Exception: {exc.args} caught")
    print("case_1_after")

    # second method
    try:
        result = list_of_numbers[5]
    except (IndexError, Exception) as exc:
        print(f"M2 - Exception: {exc.args} caught")


def case_2(name: str):
    if len(name) <= 0:
        raise ValueError("String is empty")
    print(f"Given name is : {name}")


def case_3(num: int, div: int) -> float:
    result = 0
    try:
        result = num / div
    except ZeroDivisionError as zd_exc:
        print(f"Zero exception: {zd_exc.args} caught")
        result = float(sys.maxsize)
        # result = sys.float_info.max
    return result


def case_4(dictionary: dict):
    key = "items"
    try:
        items: list = dictionary[key]
        for item in items:
            print(item)
    except KeyError as key_exc:
        print(f"Key '{key}' not found, more information: {key_exc.__traceback__}")


def case_4a(dictionary: dict):
    key = 'items'
    items: list = dictionary.get(key, [])
    for item in items:
        print(item)
    if not items:
        print(f"Key '{key}' does not exist or the list is empty")
