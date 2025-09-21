from enum import Enum

class SwitchMethod(str, Enum):
    Undefined = "Undefined"
    Level = "Level"
    Direction = "Direction"

    def __str__(self):
        return self.name