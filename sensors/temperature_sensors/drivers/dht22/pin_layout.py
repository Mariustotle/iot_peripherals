from typing import Any, Dict, Optional

from peripherals.contracts.configuration.pin_layout_base import PinLayoutBase
from peripherals.contracts.pins.pin_details import PinDetails
from peripherals.contracts.pins.pin_position import PinPosition
from peripherals.contracts.pins.pin_types import PinType

class PinLayout(PinLayoutBase):

    @staticmethod
    def get_pin_layout(adapter:Optional[Any] = None) -> Dict[PinPosition, PinDetails]:

        pin_list:Dict[PinPosition, PinDetails] = {
            PinPosition.create(horizontal_pos=1):   PinDetails.create(type=PinType.Power3V, name="+"),
            PinPosition.create(horizontal_pos=2):   PinDetails.create(type=PinType.DIGITAL, name="OUT", description="Digital Data Output"),
            PinPosition.create(horizontal_pos=3):   PinDetails.create(type=PinType.Ground, name="-")                                             
        }
        
        return pin_list
    