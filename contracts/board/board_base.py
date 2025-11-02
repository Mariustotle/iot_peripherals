


from abc import ABC, abstractmethod
from typing import Dict, Optional

from peripherals.contracts.pins.pin_details import PinDetails
from peripherals.contracts.pins.pin_position import PinPosition
from peripherals.contracts.pins.pin_types import PinType

# TODO: Use this for the base of all devices and pheripherals

class BoardBase(ABC):
    name:str = None
    pins:Dict[PinPosition, PinDetails] = None
    parent:Optional['BoardBase'] = None

    def __init__(self, parent:Optional['BoardBase'] = None):
        self.pins = {}
        self.parent = parent
        self.configure_available_pins()

    @abstractmethod
    def configure_available_pins(self):
        raise Exception(f'Please override [configure_available_pins] in the base class.')    

    
    def add_pin(self, pin_details:PinDetails, pin_position:PinPosition, name:Optional[str] = None):
        found = self.get_pin_by_position(horizontal_pos=pin_position.horizontal_position, vertical_pos=pin_position.vertical_position)
        if (found):
            raise Exception(f'[board_position=Horizontal{pin_position.horizontal_position}/Vertical={pin_position.vertical_position}] have already been added.')
        
        self.pins[pin_position] = pin_details
        self.name = name if name else pin_details.type.name

    def get_pin_by_position(self, horizontal_pos:int = 1, vertical_pos:int = 1):
        found_key = next((k for k in self.pins if k.horizontal_position == horizontal_pos and k.vertical_position == vertical_pos), None)

        return None if not found_key else self.pins.get(found_key)
