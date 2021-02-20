import json


class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"Hello, My name is {self.name} {self.surname} and I'm {self.age} years old"

    def convert_to_dict(self, items):
        try:
            with open("./human.json", "a") as fd:
                json.dump(items, fd, separators=(', ', ': '), indent=2)
        except (IOError, Exception) as e:
            print(f"Exception while writing JSON format info {e.args}")
