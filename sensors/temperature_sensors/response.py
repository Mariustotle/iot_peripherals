

from typing import Optional
from peripherals.contracts.temperature_measurement import TemperatureMeasurement
from peripherals.sensors.unit_type import UnitType
from dataclasses import dataclass

@dataclass
class DigitalTempResponse():
    temperature:float = None
    measurement:TemperatureMeasurement = None
    air_pressure:Optional[float] = None
    humidity:Optional[float] = None

    @staticmethod
    def create(temperature:float, measurement:TemperatureMeasurement, humidity:Optional[float] = None, air_pressure:Optional[float] = None, decimal_places:Optional[int] = None):
        if decimal_places:
            temperature = round(temperature, decimal_places)

            if humidity:        humidity = round(humidity, decimal_places)
            
            if air_pressure:    air_pressure = round(air_pressure, decimal_places)

        return DigitalTempResponse(temperature=temperature, measurement=measurement, humidity=humidity, air_pressure=air_pressure)

    def __str__(self):

        humidity_info = f', Humidity: {str(self.humidity)}%' if self.humidity else ''
        air_pressure_info = f', Air Pressure: {str(self.air_pressure)}' if self.air_pressure else ''

        return f'Temperature: {self.temperature if self.temperature else 'N/A '}{UnitType.Celsius.value if self.measurement == TemperatureMeasurement.Celsius else UnitType.Fahrenheit.value}{humidity_info}{air_pressure_info}'