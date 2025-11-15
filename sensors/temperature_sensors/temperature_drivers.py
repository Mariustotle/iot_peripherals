from enum import Enum

class TemperatureDrivers(str, Enum):
    Default = 'dht11'
    DHT11 = 'dht11'
    DHT22 = 'dht22'
    AHT10 = 'aht10'
