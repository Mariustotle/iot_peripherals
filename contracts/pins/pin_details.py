
from abc import ABC
from typing import Optional

from pydantic import BaseModel
from peripherals.contracts.pins.pin_types import PinType

class PinDetails(ABC, BaseModel):
    type:PinType = None
    name:Optional[str] = None
    description:Optional[str] = None
    in_use:Optional[bool] = None

    @property
    def active_pin_type(self):
        return self.type

    @property
    def label(self):
        return self.name if self.name else self.type.short
    
    @property
    def has_additional_info(self) -> bool:
        return self.description is not None or self.type.description is not None or (self.name is not None and self.name.lower() != self.type.short.lower() and self.name.lower() != self.type.value.lower())    
    
    @property
    def multi_function(self):
        return False
    
    def __str__(self):
        descript = f', Description: {self.description}' if self.description else ''

        return f'{self.label}{' (Available)' if not self.in_use else ''} >> Type: {self.type.name} [{self.type.short}]{descript}'

    @staticmethod
    def create(type:PinType, name:Optional[str] = None, description:Optional[str] = None, in_use:Optional[bool] = None):
        return PinDetails(type=type, name=name, in_use=in_use, description=description)

