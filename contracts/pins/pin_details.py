
from abc import ABC
from typing import Optional

from pydantic import BaseModel
from peripherals.contracts.pins.pin_types import PinType

class PinDetails(ABC, BaseModel):
    type:PinType = None
    label:Optional[str] = None

    @staticmethod
    def create(type:PinType, label:Optional[str] = None):
        return PinDetails(type=type, label=label)

