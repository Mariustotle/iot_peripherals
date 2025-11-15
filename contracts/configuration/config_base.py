from pydantic import BaseModel

from peripherals.peripheral_type import PeripheralType

class ConfigBase(BaseModel):
    type:str = None
    ignore:bool = False
    peripheral_type:PeripheralType = None
