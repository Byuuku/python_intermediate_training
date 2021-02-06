from figures import *


def main():
    circle1 = Circle(5)
    circle2 = Circle(12)
    circle3 = Circle(12)
    triangle1 = Triangle(7, 3)
    triangle2 = Triangle(10, 8)
    triangle3 = Triangle(5, 12)
    rectangle1 = Rectangle(4, 8)
    rectangle2 = Rectangle(14, 25)
    rectangle3 = Rectangle(10, 2)

    print(circle1.getArea())
    print(triangle1.getArea())
    print(rectangle1.getArea())
    result = Figures.check_area(100.00, [triangle1, rectangle1])
    print(result)
    print(Figures.count_area([triangle1, rectangle1]))


if __name__ == "__main__":
    main()
