from typing import Any, Dict, Optional

from peripherals.contracts.configuration.pin_layout_base import PinLayoutBase
from peripherals.contracts.pins.pin_details import PinDetails
from peripherals.contracts.pins.pin_position import PinPosition
from peripherals.contracts.pins.pin_types import PinType

class PinLayout(PinLayoutBase):

    @staticmethod
    def get_pin_layout(adapter:Optional[Any] = None) -> Dict[PinPosition, PinDetails]:

        pin_list:Dict[PinPosition, PinDetails] = {
            PinPosition.create(horizontal_pos=1):   PinDetails.create(type=PinType.ANALOG, name="A0", description="Analog temperature input"),
            PinPosition.create(horizontal_pos=2):   PinDetails.create(type=PinType.Ground),
            PinPosition.create(horizontal_pos=3):   PinDetails.create(type=PinType.Power3V, name="+", description="3.3V Power"),
            PinPosition.create(horizontal_pos=4):   PinDetails.create(type=PinType.DIGITAL, name="D0", description="Digital output for switch")                                        
        }
        
        return pin_list
    