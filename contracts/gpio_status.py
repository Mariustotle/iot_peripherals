from enum import Enum

class GPIOStatus(str, Enum):
    High = "High"
    Low = "Low"

    def __str__(self):
        return self.name