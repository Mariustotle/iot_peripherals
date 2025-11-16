from typing import Dict, Optional
from peripherals.contracts.pins.pin_details import PinDetails
from peripherals.contracts.pins.pin_position import PinPosition
from peripherals.contracts.pins.pin_types import PinType
from peripherals.sensors.tds_sensors.driver_base import TDSDriverBase

import random


class TDSSimulator(TDSDriverBase):
    min_value: int = 150
    max_value: int = 1000

    def __init__(self, config, pins:Optional[Dict[PinPosition, PinDetails]] = None):
        super().__init__(config=config, simulated=True, pins=pins)

    def read_once(self) -> float:
        random_reading = random.randint(self.min_value, self.max_value)

        return float(random_reading)
