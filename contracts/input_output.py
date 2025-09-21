from enum import Enum

class InputOutput(str, Enum):
    Undefined = "Undefined"
    Input = "Input"
    Output = "Output"

    def __str__(self):
        return self.name