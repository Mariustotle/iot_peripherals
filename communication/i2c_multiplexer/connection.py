

from pydantic import BaseModel
from peripherals.contracts.i2c_address import I2CAddress

class MultiplexerConnection(BaseModel):
    device:str = None
    address:I2CAddress = None
    channel:int = None

    def __str__(self) -> str:
        return f'{self.device} @ {self.address} (Channel {self.channel})'

    @staticmethod
    def create(device:str, address:I2CAddress, channel:int) -> 'MultiplexerConnection':
        return MultiplexerConnection(device=device, address=address, channel=channel)