from enum import Enum

class PinNumberingScheme(str, Enum):
    BOARD = "BOARD"
    BCM = "BCM"