class Cat:
    def __init__(self, name: str, sound: str = "meow, meow"):
        self.name = name
        self.sound = sound

    def make_sound(self) -> str:
        return f"Cat named {self.name} makes sound: '{self.sound}'"
