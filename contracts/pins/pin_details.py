
from abc import ABC
from typing import Optional

from pydantic import BaseModel
from peripherals.contracts.pins.pin_types import PinType

class PinDetails(ABC, BaseModel):
    type:PinType = None
    name:Optional[str] = None

    @property
    def label(self):
        return self.name if self.name else self.type.short        

    @staticmethod
    def create(type:PinType, name:Optional[str] = None):
        return PinDetails(type=type, name=name)

