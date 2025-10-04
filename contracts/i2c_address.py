from enum import Enum

class I2CAddress(str, Enum):
    Unknown = "Unkown"
    X76 = "0x76"
    X77 = "0x77"

    def __str__(self):
        return self.name