from peripherals.sensors.tds_sensors.tds_driver_base import TDSDriverBase

import random


class TDSSimulator(TDSDriverBase):
    min_value: int = 150
    max_value: int = 1000

    def read_once(self) -> float:
        random_reading = random.randint(self.min_value, self.max_value)

        return float(random_reading)