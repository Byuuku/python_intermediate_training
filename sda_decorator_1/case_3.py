from functools import wraps


def catch_io_error_decorator(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IOError as io_err:
            print(f"Caught IOError is {io_err.args}")
            return None

    return inner


def catch_io_error_with_wraps(func):
    @wraps(func)  # remember call path
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IOError as io_err:
            print(f"Caught IOError is {io_err.args}")
            return None

    return inner


@catch_io_error_decorator
def throw_exception_file():
    raise IOError("Test error")


@catch_io_error_with_wraps
def read_does_not_exist_file():
    with open("./training.training", "r") as fd:
        fd.read()
