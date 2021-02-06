from animal import Animal
from movable import Movable


class Cat(Movable, Animal):
    def __init__(self, name: str, sound: str = "meow, meow", eaten_mouse: int = 0):
        super().__init__(name, sound)
        self.eaten_mouse = eaten_mouse

    def make_sound(self) -> str:
        return f"Cat named {self.name} makes sound: '{self.sound}'"

    def eat_mouse(self) -> int:
        self.eaten_mouse += 1
        return self.eaten_mouse

    def count_eaten_mouse(self) -> int:
        print(f"{self.name} ate {self.eaten_mouse} mouses")
        return self.eaten_mouse

    def move(self) -> str:
        return "I am walking on roofs"
