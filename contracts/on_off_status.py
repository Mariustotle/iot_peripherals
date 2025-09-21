from enum import Enum

class OnOffStatus(str, Enum):
    On = "On"
    Off = "Off"

    def __str__(self):
        return self.name