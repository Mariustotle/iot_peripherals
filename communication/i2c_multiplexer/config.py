from typing import Optional
from pydantic import BaseModel

from peripherals.contracts.i2c_address import I2CAddress

class I2CMultiplexerConfig(BaseModel):
    name: str = None
    multiplexer_address: I2CAddress = I2CAddress.Unknown
    number_of_channels: Optional[int] = None

    


