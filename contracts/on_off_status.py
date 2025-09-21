from enum import Enum

class OnOffStatus(str, Enum):
    Unkown = "Unknown"
    On = "On"
    Off = "Off"

    def __str__(self):
        return self.name