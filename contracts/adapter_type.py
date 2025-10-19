
from enum import Enum

class AdapterType(str, Enum):
    Unknown = "Unknown"
    RaspberryOSTrixy = 'RaspberryOSTrixy'

    def __str__(self):
        return self.name

