from typing import Optional
from enum import Enum
from pydantic import BaseModel, model_validator

class PinNumberingScheme(str, Enum):
    BOARD = "BOARD"
    BCM = "BCM"

class PinConfig(BaseModel):
    pin: int
    name: Optional[str] = None
    scheme: PinNumberingScheme = PinNumberingScheme.BOARD

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