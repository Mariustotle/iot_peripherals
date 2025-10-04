

from typing import Optional
from peripherals.contracts.temperature_measurement import TemperatureMeasurement
from peripherals.sensors.unit_type import UnitType
from dataclasses import dataclass

@dataclass
class DigitalComboResponse():
    temperature:float = None
    measurement:TemperatureMeasurement = None
    air_pressure:Optional[float] = None
    hygrometer:Optional[float] = None

    @staticmethod
    def create(temperature:float, measurement:TemperatureMeasurement, air_pressure:Optional[float] = None, hygrometer:Optional[float] = None):
        return DigitalComboResponse(temperature=temperature, measurement=measurement, air_pressure=air_pressure, hygrometer=hygrometer)

    def __str__(self):

        air_pressure_info = f', Air Pressure: [{str(self.air_pressure)}]' if self.air_pressure is not None else ''
        hygrometer_info = f', Hygrometer: [{str(self.hygrometer)}]' if self.hygrometer is not None else ''

        return f'Temperature: {self.temperature} {UnitType.Celsius if self.measurement == TemperatureMeasurement.Celsius else UnitType.Fahrenheit}{air_pressure_info}{hygrometer_info}'