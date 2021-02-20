def catch_io_error_decorator(func):
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
