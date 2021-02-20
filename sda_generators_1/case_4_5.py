from time import sleep


def lazy_read_generator(fd, text_size=1024):
    while True:
        result = fd.read(text_size)
        if not result:
            break
        yield result


def generator_ex_4():
    print("Exercise 4")
    with open("./lorem_ipsum.txt", "r") as fd:
        for line in lazy_read_generator(fd):
            sleep(2)
            print(line)


def reader_line_by_line():
    for line in open("./lorem_ipsum.txt", "r"):
        yield line
