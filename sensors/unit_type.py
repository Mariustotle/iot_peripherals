from enum import Enum

class UnitType(str, Enum):
    Unkown = "Unkown"
    TDS = "ppm"
    Celsius = "°C"
    Fahrenheit = "°F"
    