from peripherals.communication.i2c_expander.i2c_expander_drivers import I2CExpanderDrivers
from pydantic import BaseModel
from typing import Optional


class I2CExpanderConfig(BaseModel):
    name: str = None
    driver: Optional[I2CExpanderDrivers] = None
    i2c_bus: int = None
    i2c_address: int = None
    


