
from abc import ABC
from typing import Optional

from pydantic import BaseModel
from peripherals.contracts.pins.pin_types import PinType

class PinDetails(ABC, BaseModel):
    type:PinType = None
    name:Optional[str] = None
    in_use:bool = None

    @property
    def label(self):
        return self.name if self.name else self.type.short
    
    @property
    def multi_function(self):
        return False

    @staticmethod
    def create(type:PinType, name:Optional[str] = None, in_use:bool = False):
        return PinDetails(type=type, name=name, in_use=in_use)

