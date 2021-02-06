from abc import abstractmethod, ABC


def count_area(*args):
    area = 0.0
    for arg in args:
        area += arg.getArea()
    return area
