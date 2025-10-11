
from enum import Enum

class DeviceType(str, Enum):
    Unknown = "Unkown"
    RaspberryPi3  = "Raspberry Pi 3"
    RaspberryPi4 = "Raspberry Pi 4"
    RaspberryPi5 = "Raspberry Pi 5"
    RaspberryPiZero = "Raspberry Pi Zero"
    RaspberryPiPico = "Raspberry Pi Pico"
    ArduinoUno = "ArduinoUno"
    ArduinoMega = "ArduinoMega"
    ArduinoNano = "ArduinoNano"
    ESP32 = "ESP32"
    ESP8266 = "ESP8266"

    def __str__(self):
        return self.name

