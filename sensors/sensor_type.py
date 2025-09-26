from enum import Enum

class SensorType(str, Enum):
    TDS = "TDS"
    DigitalTemperature = "DigitalTemperature"
    TempAndHumidity = "TempAndHumidity"
    Other = "Other"