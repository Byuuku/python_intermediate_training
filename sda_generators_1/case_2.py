def number_creator(n):
    list_of_numbers = []
    for number in range(n):
        list_of_numbers.append(number)
    return list_of_numbers


def iterator_ex_2(n):
    import sys
    result_list = number_creator(n)
    print(f"Size of list in bytes: {sys.getsizeof(result_list)}")
    result = sum(result_list)
    print(f"Size of one number in bytes: {sys.getsizeof(1)}")
    print(result)
