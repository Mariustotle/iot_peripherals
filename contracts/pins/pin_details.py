
from abc import ABC
from typing import Optional

from pydantic import BaseModel
from peripherals.contracts.pins.pin_position import PinPosition
from peripherals.contracts.pins.pin_types import PinType

class PinDetails(ABC, BaseModel):
    type:PinType = None
    label:Optional[str] = None
    source_pin:Optional[PinPosition] = None

    @staticmethod
    def create(type:PinType, label:Optional[str] = None, source_pin:Optional[PinPosition] = None):
        return PinDetails(type=type, label=label, source_pin=source_pin)

