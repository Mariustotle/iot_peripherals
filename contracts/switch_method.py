from enum import Enum

class SwitchMethod(str, Enum):
    Level = "Level"
    Direction = "Direction"

    def __str__(self):
        return self.name