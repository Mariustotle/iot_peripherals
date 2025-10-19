from typing import Optional
from enum import Enum
from pydantic import BaseModel, model_validator
from peripherals.contracts.pins.pin_numbering_scheme import PinNumberingScheme
from peripherals.contracts.pins.pin_types import PinType

class PinConfig(BaseModel):
    pin: int
    name: Optional[str] = None
    scheme: PinNumberingScheme = PinNumberingScheme.BOARD
    type:Optional[PinType] = PinType.Default

    def set_type(self, new_type: PinType) -> None:
        self.type = new_type

    def __str__(self):
        return f'{self.name} (Device Pin {self.pin} - {self.scheme.name})'

    @model_validator(mode="before")
    @classmethod
    def coerce(cls, value):
        if isinstance(value, int):
            return {"pin": value}
        return value
    


'''
# Simple Usage
"gpio_pin": 12

# Advance Usage
"gpio_pin": {
    "pin": 12,
    "scheme": "BOARD",
    "name": "Light Relay"
}
'''