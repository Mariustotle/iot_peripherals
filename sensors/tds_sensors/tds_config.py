from pydantic import BaseModel
from typing import Optional

from peripherals.sensors.tds_sensors.tds_drivers import TDSDrivers


class TDSConfig(BaseModel):

    gpio_pin: int = None
    driver: Optional[TDSDrivers] = None
    name: str = None
