from datetime import date

from person import Person
from employee import Employee
from manager import Manager


def main():
    employee = Employee("Jan", "Kowalski", date(1985, 12, 21))

    print(employee.birth_date)


if __name__ == "__main__":
    main()
