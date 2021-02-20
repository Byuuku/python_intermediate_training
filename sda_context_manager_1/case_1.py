from contextlib import contextmanager


@contextmanager
def open_file(path: str, mode="a"):
    print("Opening file")
    fd = open(path, mode)
    yield fd
    fd.close()
    print("Closing file")


def exercise_1():
    try:
        with open_file("./context_manager_file.txt") as fd:
            fd.write("This is an example text, check it on the created file")
    except IOError as io_err:
        print(f"IO exception found, more info {io_err.args}")
