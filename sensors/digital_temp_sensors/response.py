

from typing import Optional
from peripherals.contracts.temperature_measurement import TemperatureMeasurement
from peripherals.sensors.unit_type import UnitType
from dataclasses import dataclass

@dataclass
class DigitalTempResponse():
    temperature:float = None
    measurement:TemperatureMeasurement = None
    humidity:Optional[float] = None    

    @staticmethod
    def create(temperature:float, measurement:TemperatureMeasurement, humidity:Optional[float] = None):
        return DigitalTempResponse(temperature=temperature, measurement=measurement, humidity=humidity)

    def __str__(self):

        humidity_info = f', Humidity: [{str(self.humidity)}]' if self.humidity is not None else ''

        return f'Temperature: {self.temperature if self.temperature else 'N/A'} {UnitType.Celsius if self.measurement == TemperatureMeasurement.Celsius else UnitType.Fahrenheit}{humidity_info}'