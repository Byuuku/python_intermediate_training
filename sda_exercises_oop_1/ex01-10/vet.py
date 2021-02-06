from animal import Animal
from cat import Cat
from dog import Dog


class Vet:

    @classmethod
    def say_cat_hello(cls, cat: Cat) -> str:
        return f"Hello, cute {cat.name}!"

    @classmethod
    def say_dog_hello(cls, dog: Dog) -> str:
        return f"Hello, brave {dog.name}!"

    @classmethod
    def say_hello(cls, animal: Animal) -> str:
        return f"Hello, {animal.name}"
