from person import Person
from datetime import date


class Employee(Person):
    def __init__(self, name: str, surname: str, birth_date: date, salary=1000.0):
        super().__init__(name, surname, birth_date)
        self._salary = salary

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value: date):
        value = self.check_date(value)
        self._birth_date = value

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value: float):
        self._salary = value

    @staticmethod
    def check_date(value: date) -> date:
        if value < date(year=1900, month=1, day=1) or value > date(year=2020, month=12, day=31):
            value = date(0, 0, 0)
        return value

    def who_am_i(self):
        print(f"Employee name is {self.name} {self.surname} and he earns {self.salary} dollars")

