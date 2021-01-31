class Cat:
    def __init__(self, name: str, sound: str = "meow, meow", eaten_mouse: int = 0):
        self.name = name
        self.sound = sound
        self.eaten_mouse = eaten_mouse

    def make_sound(self) -> str:
        return f"Cat named {self.name} makes sound: '{self.sound}'"

    def eat_mouse(self) -> int:
        self.eaten_mouse += 1
        print(f"I ate {self.eaten_mouse} mouses")
        return self.eaten_mouse
