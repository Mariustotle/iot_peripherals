
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from peripherals.contracts.board.pin_association import PinAssociation
from peripherals.contracts.pins.pin_details import PinDetails
from peripherals.contracts.pins.pin_display import PinDisplay
from peripherals.contracts.pins.pin_position import PinPosition
from peripherals.contracts.pins.pin_types import PinType

class BoardBase(ABC):
    name:str = None
    pins:Dict[PinPosition, PinDetails] = None
    parent:Optional['BoardBase'] = None
    associated_pins:Dict[PinPosition, PinAssociation] = None
    default_use_state:bool = True
    default_pin_type:Optional[PinType] = None

    def __init__(self, name:str, parent:Optional['BoardBase'] = None, default_pin_type:Optional[PinType]=None, default_use_state:bool = True, pins:Optional[Dict[PinPosition, PinDetails]] = None):
        self.name = name
        self.pins = {}
        self.associated_pins = {}
        self.parent = parent
        self.default_use_state = default_use_state
        self.default_pin_type = default_pin_type

        self._configure_pins(pins)
       
    def _configure_pins(self, pins:Optional[Dict[PinPosition, PinDetails]] = None):
        if pins is None or len(pins) == 0:
            # No pins to configure
            return

        for position, details in pins.items():
            self.add_pin(pin_position=position, pin_details=details)
   
    def add_pin(self, pin_details:PinDetails, pin_position:PinPosition):
        (position, found_pin) = self.get_pin_by_position(horizontal_pos=pin_position.horizontal_position, vertical_pos=pin_position.vertical_position)

        if (found_pin):
            raise Exception(f'[board_position=Horizontal{pin_position.horizontal_position}/Vertical={pin_position.vertical_position}] have already been added.')
        
        if pin_details.in_use is None:
            pin_details.in_use = self.default_use_state
        
        self.pins[pin_position] = pin_details


    def associate_pin(self, my_position:PinPosition, type:PinType):

        if (type == PinType.Default and self.default_pin_type is not None):
            type = self.default_pin_type

        # Find destination pin
        (position, pin_details) = self.get_pin_by_position(horizontal_pos=my_position.horizontal_position, vertical_pos=my_position.vertical_position)

        if pin_details is None:
            raise Exception(f'Unable to associate PIN [{my_position}] on [{self.name}] as the PIN does not exist on [{self.name}]') 

        if (pin_details.in_use):
            raise Exception(f'Unable to associate PIN [{my_position}] on [{self.name}] as the PIN is already in use on [{self.name}]')
        
        if pin_details.active_pin_type != type:
            raise Exception(f'Unable to associate PIN [{my_position}] on [{self.name}] as request type [{type.name}] does not match the current PIN type [{pin_details.active_pin_type}]')
        
        pin_details.in_use = True

        '''
        if (not pin_details):
            raise Exception(f'Unable to associate PIN [{other_position}] from [{source.name}] to [{self.name}] PIN [{my_position}] as the PIN does not exist on [{self.name}]')
        
        if (pin_details.type != type):
            raise Exception(f'Unable to associate PIN [{other_position}] from [{source.name}] to [{self.name}] PIN [{my_position}] as request type [{type.name}] does not match the current PIN type [{pin_details.type}]')
        
         self.associated_pins[position] = PinAssociation.create(source=source, other_position=other_position, my_position=position, type=type)
        '''


    def get_pin_by_position(self, horizontal_pos:int = 1, vertical_pos:int = 1):
        position  = next((k for k in self.pins if k.horizontal_position == horizontal_pos and k.vertical_position == vertical_pos), None)

        return (None, None) if not position else (position, self.pins.get(position))
    

    def get_pin_display_matrix(self) -> List[List[PinDisplay]]:

        # Determine the full coordinate range
        all_h = [p.horizontal_position for p in self.pins.keys()]
        all_v = [p.vertical_position for p in self.pins.keys()]
        max_h = max(all_h)
        max_v = max(all_v)

        # Create a 2D matrix covering the entire range (inclusive of both min and max)
        matrix = [[None for _ in range(max_h)] for _ in range(max_v)]

        # Iterate through every possible coordinate permutation (v, h)
        for v in range(1, max_v+1):
            for h in range(1, max_h+1):
                # Find pin with these coordinates
                (position, pin) = self.get_pin_by_position(horizontal_pos=h, vertical_pos=v)

                matrix[v-1][h-1] = None if not pin else PinDisplay.create(name=pin.label, in_use=pin.in_use, multi_function=pin.multi_function)

        return matrix