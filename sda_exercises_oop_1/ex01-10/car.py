from movable import Movable


class Car(Movable):

    def move(self) -> str:
        return f"I am riding"
