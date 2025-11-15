
import random
from peripherals.sensors.tds_sensors.driver_base import TDSDriverBase


class GENERIC(TDSDriverBase):
    min_value: int = 150
    max_value: int = 1000

    def read_once(self) -> float:
        random_reading = random.randint(self.min_value, self.max_value)

        return float(random_reading)