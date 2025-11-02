
from abc import ABC, abstractmethod
from typing import Dict, Optional

from peripherals.contracts.board.pin_association import PinAssociation
from peripherals.contracts.pins.pin_details import PinDetails
from peripherals.contracts.pins.pin_position import PinPosition
from peripherals.contracts.pins.pin_types import PinType

# TODO: Use this for the base of all devices and pheripherals

class BoardBase(ABC):
    name:str = None
    pins:Dict[PinPosition, PinDetails] = None
    parent:Optional['BoardBase'] = None
    associated_pins:Dict[PinPosition, PinAssociation] = None

    def __init__(self, name:str, parent:Optional['BoardBase'] = None):
        self.name = name
        self.pins = {}
        self.associated_pins = {}
        self.parent = parent
        self.configure_available_pins()

    @abstractmethod
    def configure_available_pins(self):
        raise Exception(f'Please override [configure_available_pins] in the base class.')
    
    def add_pin(self, pin_details:PinDetails, pin_position:PinPosition, name:Optional[str] = None):
        (position, found_pin) = self.get_pin_by_position(horizontal_pos=pin_position.horizontal_position, vertical_pos=pin_position.vertical_position)

        if (found_pin):
            raise Exception(f'[board_position=Horizontal{pin_position.horizontal_position}/Vertical={pin_position.vertical_position}] have already been added.')
        
        self.pins[pin_position] = pin_details


    def associate_pin(self, source:'BoardBase', other_position:PinPosition, my_position:PinPosition, type:PinType):

        # Find destination pin
        (position, pin_details) = self.get_pin_by_position(horizontal_pos=my_position.horizontal_position, vertical_pos=my_position.vertical_position)

        if (not pin_details):
            raise Exception(f'Unable to associate PIN [{other_position}] from [{source.name}] to [{self.name}] PIN [{my_position}] as the PIN does not exist on [{self.name}]')
        
        if (pin_details.type != type):
            raise Exception(f'Unable to associate PIN [{other_position}] from [{source.name}] to [{self.name}] PIN [{my_position}] as request type [{type.name}] does not match the current PIN type [{pin_details.type}]')
        
        self.associated_pins[position] = PinAssociation.create(source=source, other_position=other_position, my_position=position, type=type)



    def get_pin_by_position(self, horizontal_pos:int = 1, vertical_pos:int = 1):
        position  = next((k for k in self.pins if k.horizontal_position == horizontal_pos and k.vertical_position == vertical_pos), None)

        return (None, None) if not position else (position, self.pins.get(position))
