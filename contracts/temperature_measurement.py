from enum import Enum

class TemperatureMeasurement(str, Enum):
    Undefined = "Undefined"
    Celsius = "Celsius"
    Fahrenheit = "Fahrenheit"

    def __str__(self):
        return self.name