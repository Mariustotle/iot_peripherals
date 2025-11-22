from enum import Enum

class I2CAddress(str, Enum):
    Unknown = None
    X76 = 0x76
    X77 = 0x77
    X38 = 0x38

    def __str__(self):
        return self.name