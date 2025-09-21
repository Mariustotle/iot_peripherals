from enum import Enum

class InputOutput(str, Enum):
    Input = "Input"
    Output = "Output"

    def __str__(self):
        return self.name