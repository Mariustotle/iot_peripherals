from peripherals.contracts.pins.pin_details import PinDetails
from peripherals.contracts.pins.pin_position import PinPosition
from peripherals.contracts.pins.pin_types import PinType
from peripherals.contracts.temperature_measurement import TemperatureMeasurement
from peripherals.sensors.digital_i2c_combo_sensor.driver_base import DigitalComboDriverBase

import random

from peripherals.sensors.digital_i2c_combo_sensor.response import DigitalComboResponse

class DigitalComboSimulator(DigitalComboDriverBase):

    def __init__(self, config, simulated = False):
        super().__init__(config, simulated)

    def generate_air_pressure(self):
        """
        Simulates realistic sea-level air pressure in hPa.
        Normal range: 980 - 1050 hPa
        """
        base = 1013.25  # average sea-level pressure
        return round(random.gauss(mu=base, sigma=5), 2)  # Gaussian distribution for realism

    def generate_humidity(self):
        """
        Simulates realistic relative humidity in %.
        Normal indoor range: 20 - 70%
        """
        return round(random.uniform(30, 65), 1)  # Uniform within a comfortable indoor range

    def _default_reading(self) -> float:

        measurement = 0.0

        # Assume typical room temperature range
        if self.config.measurement == TemperatureMeasurement.Celsius:
            # Room temperature between 18°C and 26°C
            measurement = round(random.uniform(18.0, 26.0), 2)
        
        elif self.unit == "Fahrenheit":
            # Equivalent in Fahrenheit (65°F to 79°F)
            measurement = round(random.uniform(65.0, 79.0), 2)

        air_pressure = self.generate_air_pressure()
        hygrometer = self.generate_humidity()       
        

        return DigitalComboResponse.create(
            temperature=measurement,
            measurement=self.config.measurement,
            air_pressure=air_pressure,
            hygrometer=hygrometer
        )

    def configure_available_pins(self):
        
        self.add_pin(
            pin_position=PinPosition.create(horizontal_pos=1),
            pin_details=PinDetails.create(type=PinType.Ground)            
        )
