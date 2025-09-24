from pydantic import BaseModel
from typing import Optional

from peripherals.sensors.tds_sensors.tds_drivers import TDSDrivers


class TDSConfig(BaseModel):
    name: str = None
    analog_digital_converter_name: str = None
    adc_channel: int = None
    number_of_readings: Optional[int] = 1
    delay_between_readings: float = 0.0
    driver: Optional[TDSDrivers] = None
