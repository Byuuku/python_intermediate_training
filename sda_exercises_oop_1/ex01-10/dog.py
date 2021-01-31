class Dog:
    def __init__(self, name: str, sound: str = "hau, hau"):
        self.name = name
        self.sound = sound

    def make_sound(self) -> str:
        return f"Dog named {self.name} makes sound: '{self.sound}'"
