
import random
from peripherals.sensors.tds_sensors.tds_driver_base import TDSDriverBase


class TDS_METER_V1(TDSDriverBase):
    min_value: float = 150.0
    max_value: float = 1000.0

    async def read_once(self) -> float:
        return random.randint(self.min_value, self.max_value)