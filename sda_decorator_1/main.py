def main():
    print("Step: 3 - Function - main")
    a, b = print_hello_world(24, 65)
    print(f"Step: 8 - In Function - main, a = {a} and b = {b} arguments")


def wrap_before_and_after(func):
    print("Step: 1 - Function - wrap_before_and_after")

    def wrapper(*args, **kwargs):
        print("Step: 4 - Before func results")
        result = func(*args, **kwargs)
        print("Step: 7 - After func results")
        return result

    print("Step: 2 - Return function - wrapper")
    return wrapper


@wrap_before_and_after
def print_hello_world(a, b):
    print("Step: 5 - Hello, world!")
    print(f"Step: 6 - {a, b}")
    return a, b


if __name__ == "__main__":
    main()
