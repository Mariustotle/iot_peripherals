

from peripherals.contracts.temperature_measurement import TemperatureMeasurement
from peripherals.sensors.unit_type import UnitType
from dataclasses import dataclass

@dataclass
class DigitalTempResponse():
    humidity:float = None
    temperature:float = None
    measurement:TemperatureMeasurement = None

    @staticmethod
    def create(temperature:float, measurement:TemperatureMeasurement, humidity:float):
        return DigitalTempResponse(temperature=temperature, measurement=measurement, humidity=humidity)

    def __str__(self):
        return f'Temperature: {self.temperature} {UnitType.Celsius if self.measurement == TemperatureMeasurement.Celsius else UnitType.Fahrenheit}, Humidity: {self.humidity}'