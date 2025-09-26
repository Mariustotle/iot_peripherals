from enum import Enum

class DigitalTempDrivers(str, Enum):
    Default = 'ds18b20'
    DS18B20 = 'ds18b20'             # Standard Digital Temperature Sensor
