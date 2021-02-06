from math import pi

from figure import Figure

from abc import ABC, abstractmethod


class Figures(ABC):
    @abstractmethod
    def getArea(self):
        pass

    @staticmethod
    def count_area(figure_list: list) -> float:
        area = 0.0
        for figure in figure_list:
            area += figure.getArea()
        return area

    @staticmethod
    def check_area(area: float, figure_list: list) -> bool:
        figure_area = Figures.count_area(figure_list)
        return area > figure_area


class Rectangle(Figures):

    def __init__(self, high: float, width: float):
        self.high = high
        self.width = width

    def getArea(self):
        return self.high * self.width


class Circle(Figures):
    def __init__(self, radius: float):
        self.radius = radius

    def getArea(self):
        return round(self.radius * self.radius * pi, 4)


class Triangle(Figures):

    def __init__(self, high: float, base: float):
        self.high = high
        self.base = base

    def getArea(self):
        return (self.high * self.base) / 2.0