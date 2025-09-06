from enum import Enum

class PeripheralType(str, Enum):
    Undefined = "Undefined"
    Sensor = "Sensor"
    Actuator = "Actuator"
    Communication = "Communication"
    Display = "Display"