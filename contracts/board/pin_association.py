
from typing import Any
from pydantic import BaseModel
from peripherals.contracts.pins.pin_position import PinPosition
from peripherals.contracts.pins.pin_types import PinType


class PinAssociation(BaseModel):
    source:Any              = None
    other_position:PinPosition      = None
    my_position:PinPosition         = None
    type:PinType                    = None

    @staticmethod
    def create(source:Any, other_position:PinPosition, my_position:PinPosition, type:PinType):
        return PinAssociation(source=source, other_position=other_position, my_position=my_position, type=type)