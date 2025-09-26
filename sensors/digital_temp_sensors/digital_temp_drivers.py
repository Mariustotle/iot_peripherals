from enum import Enum

class DigitalTempDrivers(str, Enum):
    Default = 'dht22'
    DHT22 = 'dht22'             # HW-503 Common thermistor + LM393 Comparator module
