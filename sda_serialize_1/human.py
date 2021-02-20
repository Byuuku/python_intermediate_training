import json


class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"Hello, My name is {self.name} {self.surname} and I'm {self.age} years old"

    def convert_to_dict(self):
        return self.__dict__

    @classmethod
    def convert_from_dict(cls, params: dict):
        name = params.get("name", "-")
        surname = params.get("surname", "-")
        age = params.get("age", 0)

        return cls(name, surname, age)


def json_human_write(humans: list):
    humans_serialize = []

    for human in humans:
        human_dict = human.convert_to_dict()
        humans_serialize.append(human_dict)

    try:
        with open("./human.json", "a") as fd:
            json.dump(humans_serialize, fd, indent=2)
    except (IOError, Exception) as e:
        print(f"Exception while writing JSON format info {e.args}")


def json_human_read():
    humans_serialize = []

    try:
        with open("./human.json", "r") as fd:
            humans_serialize = json.load(fd)
    except (IOError, Exception) as e:
        print(f"Exception while writing JSON format info {e.args}")

    humans_final = []
    for human_dict in humans_serialize:
        human = Human.convert_from_dict(human_dict)
        humans_final.append(human)
    return humans_final
