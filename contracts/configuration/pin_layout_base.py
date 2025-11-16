from abc import abstractmethod
from typing import Any, Dict, Optional

from pydantic import BaseModel

from peripherals.contracts.pins.pin_details import PinDetails
from peripherals.contracts.pins.pin_position import PinPosition

class PinLayoutBase(BaseModel):

    @staticmethod
    @abstractmethod
    def get_pin_layout(adapter:Optional[Any] = None) -> Dict[PinPosition, PinDetails]: pass

       