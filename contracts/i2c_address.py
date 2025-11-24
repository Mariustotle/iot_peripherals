from enum import Enum

class I2CAddress(int, Enum):
    Unknown = 0
    X76 = 0x76   # 118
    X77 = 0x77   # 119
    X38 = 0x38   # 56

    def __str__(self):
        return self.name