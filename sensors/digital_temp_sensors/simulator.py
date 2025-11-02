from peripherals.contracts.pins.pin_details import PinDetails
from peripherals.contracts.pins.pin_position import PinPosition
from peripherals.contracts.pins.pin_types import PinType
from peripherals.contracts.temperature_measurement import TemperatureMeasurement
from peripherals.sensors.digital_temp_sensors.driver_base import DigitalTempDriverBase

import random

class DigitalTempSimulator(DigitalTempDriverBase):

    def __init__(self, config, simulated = False):
        super().__init__(config, simulated)

    def _default_reading(self) -> float:

        # Assume typical room temperature range
        if self.config.measurement == TemperatureMeasurement.Celsius:
            # Room temperature between 18°C and 26°C
            return round(random.uniform(18.0, 26.0), 2)
        
        elif self.unit == "Fahrenheit":
            # Equivalent in Fahrenheit (65°F to 79°F)
            return round(random.uniform(65.0, 79.0), 2)
        
        

    def configure_available_pins(self):
        
        self.add_pin(
            pin_position=PinPosition.create(horizontal_pos=1),
            pin_details=PinDetails.create(type=PinType.Ground, label='G')            
        )
        self.add_pin(
            pin_position=PinPosition.create(horizontal_pos=2),
            pin_details=PinDetails.create(type=PinType.DIGITAL, label='D')            
        )
        self.add_pin(
            pin_position=PinPosition.create(horizontal_pos=3),
            pin_details=PinDetails.create(type=PinType.Power3V, label='V')            
        )