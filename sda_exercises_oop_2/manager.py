from employee import Employee
from datetime import date


class Manager(Employee):
    def __init__(self, name: str, surname: str, birth_date: date, salary=1000.0):
        super().__init__(name, surname, birth_date, salary)
        self._salary = salary * 1.1

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value: float):
        self._salary = value * 1.1

    def who_am_i(self):
        print(f"manager name is {self.name} {self.surname} and he earns {self.salary} dollars")