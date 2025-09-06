from peripherals.communication.i2c_expander.i2c_expander_drivers import I2CExpanderDrivers
from pydantic import BaseModel
from typing import Optional


class I2CExpanderConfig(BaseModel):

    driver: Optional[I2CExpanderDrivers] = None
    name: str = None


