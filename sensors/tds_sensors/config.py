from typing import Optional

from peripherals.sensors.tds_sensors.tds_drivers import TDSDrivers
from src.contracts.modules.analog_base import AnalogBase


class TDSConfig(AnalogBase):
    name: str = None
    number_of_readings: Optional[int] = 1
    delay_between_readings: float = 0.0
    driver: Optional[TDSDrivers] = None
