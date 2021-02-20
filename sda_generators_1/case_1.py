def iterator_ex_1():
    dictionary = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4
    }

    for key in dictionary.keys():
        print(key)

    for value in dictionary.values():
        print(value)
