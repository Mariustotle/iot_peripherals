import random
from typing import Any, Optional, Dict
from peripherals.contracts.pins.pin_details import PinDetails
from peripherals.contracts.pins.pin_position import PinPosition
from peripherals.contracts.pins.pin_types import PinType
from peripherals.contracts.temperature_measurement import TemperatureMeasurement
from peripherals.sensors.temperature_switch.config import TempSwitchConfig
from peripherals.sensors.temperature_switch.driver_base import TempSwitchDriverBase

class LM393(TempSwitchDriverBase):

    def __init__(self, config:TempSwitchConfig, simulated:bool = False, pins:Optional[Dict[PinPosition, PinDetails]] = None):
        super().__init__(config, simulated, pins)

    def _default_reading(self) -> float:

        # Assume typical room temperature range
        if self.config.measurement == TemperatureMeasurement.Celsius:
            # Room temperature between 18°C and 26°C
            return round(random.uniform(18.0, 26.0), 2)
        
        elif self.unit == "Fahrenheit":
            # Equivalent in Fahrenheit (65°F to 79°F)
            return round(random.uniform(65.0, 79.0), 2)
    