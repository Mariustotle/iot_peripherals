from typing import Dict, Optional
from peripherals.contracts.pins.pin_details import PinDetails
from peripherals.contracts.pins.pin_position import PinPosition
from peripherals.contracts.pins.pin_types import PinType
from peripherals.contracts.temperature_measurement import TemperatureMeasurement
from peripherals.sensors.temperature_sensors.driver_base import TemperatureDriverBase

import random

from peripherals.sensors.temperature_sensors.response import DigitalTempResponse

class TemperatureSimulator(TemperatureDriverBase):

    def __init__(self, config, pins:Optional[Dict[PinPosition, PinDetails]] = None):
        super().__init__(config, True, pins=pins)

    def _default_reading(self) -> float:

        temperature:float = None
        humidity:float = None

        humidity = round(random.uniform(70.0, 80.0), 5) 

        # Assume typical room temperature range
        if self.config.measurement == TemperatureMeasurement.Celsius:
            temperature = round(random.uniform(18.0, 26.0), 4)        
        elif self.config.measurement == TemperatureMeasurement.Fahrenheit:
            temperature =  round(random.uniform(65.0, 79.0), 4)

        return DigitalTempResponse.create(
            temperature=temperature,
            measurement=self.config.measurement,
            humidity=humidity,
            decimal_places=self.config.number_of_decimal_places
        )
