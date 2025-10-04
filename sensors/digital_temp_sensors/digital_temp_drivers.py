from enum import Enum

class DigitalTempDrivers(str, Enum):
    Default = 'dht11'
    DHT11 = 'dht11'
    DHT22 = 'dht22'
    BME280 = 'bme280'
