from sda_decorator_1.case_2 import read_file
from sda_decorator_1.case_3 import throw_exception_file

def main():
#     print("Step: 3 - Passing 'main' arguments to 'print_hello_world'")
#     a, b = print_hello_world(24, 65)
#     print(f"Step: 8 - In 'main' function arguments: a = {a} and b = {b}")
#
#
# def wrap_before_and_after(func):
#     print("Step: 1 - Function 'wrap_before_and_after'")
#
#     def wrapper(*args, **kwargs):
#         print("Step: 4 - Before passing 'func' arguments")
#         result = func(*args, **kwargs)
#         print("Step: 7 - After passing 'func' arguments")
#         return result
#
#     print("Step: 2 - Go to 'wrapper' function")
#     return wrapper

    # read_file(file_path="./abc")


# @wrap_before_and_after
# def print_hello_world(a, b):
#     print("Step: 5 - Print: Hello, world!")
#     print(f"Step: 6 - Print: 'print_hello_world' function arguments {a, b} from Step 3: 'main' function")
#     return a, b

    throw_exception_file()


if __name__ == "__main__":
    main()
