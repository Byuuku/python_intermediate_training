import pytest
from figures import Figures, Circle, Triangle, Rectangle


def test_check_area():
    #  given
    circle1 = Circle(1)
    triangle1 = Triangle(2, 1)
    rectangle1 = Rectangle(2, 2)

    #  when
    result = Figures.count_area([circle1, triangle1, rectangle1])

    #  then
    assert result == 8.1416
