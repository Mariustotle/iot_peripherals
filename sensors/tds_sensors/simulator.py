from peripherals.contracts.pins.pin_details import PinDetails
from peripherals.contracts.pins.pin_position import PinPosition
from peripherals.contracts.pins.pin_types import PinType
from peripherals.sensors.tds_sensors.driver_base import TDSDriverBase

import random


class TDSSimulator(TDSDriverBase):
    min_value: int = 150
    max_value: int = 1000

    def __init__(self, config, simulated = False):
        super().__init__(config, simulated)

    def read_once(self) -> float:
        random_reading = random.randint(self.min_value, self.max_value)

        return float(random_reading)
    

    def configure_available_pins(self):
        
        self.add_pin(
            pin_position=PinPosition.create(horizontal_pos=1),
            pin_details=PinDetails.create(type=PinType.Ground)            
        )
        self.add_pin(
            pin_position=PinPosition.create(horizontal_pos=2),
            pin_details=PinDetails.create(type=PinType.ANALOG)            
        )
        self.add_pin(
            pin_position=PinPosition.create(horizontal_pos=3),
            pin_details=PinDetails.create(type=PinType.Power3V)            
        )
