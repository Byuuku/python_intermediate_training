class Cat:
    def __init__(self, name: str):
        self.name = name

    def make_sound(self) -> str:
        return f"Cat named {self.name} does 'meowww meowww meowwwwww'"
