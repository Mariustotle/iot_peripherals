from abc import abstractmethod
from typing import Optional, Any, Dict
from common.environment import Env
from peripherals.contracts.board.board_base import BoardBase
from peripherals.contracts.pins.pin_details import PinDetails
from peripherals.contracts.pins.pin_position import PinPosition
from peripherals.peripheral_type import PeripheralType

class Peripheral(BoardBase):
    peripheral_type: PeripheralType = None
    config:Any = None
    simulated:bool = None
    driver_name:str = None
    
    @property
    def key(self) -> str:
        return f'{self.peripheral_type.value}-{self.name}'
    
    def __init__(self, simulated:bool, peripheral_type:PeripheralType, name:str, parent:Optional['BoardBase'] = None, config:Any = None, pins:Optional[Dict[PinPosition, PinDetails]] = None):
        self.peripheral_type = peripheral_type
        self.config = config
        self.simulated = simulated

        super().__init__(name=name, parent=parent, pins=pins)

    @abstractmethod
    def get_description(self) -> str: pass

    def initialize(self) -> bool:
        try:
            return self._initialize(self.name, self.config)
        
        except Exception as ex:
            print(f"Unable to initialize {self.name} of type [{self.peripheral_type}]. Error details: {ex}")
            return False
                        
    
    def _initialize(self, name:str, config:Optional[Any] = None) -> bool:
        Env.print(f'Default initialization for {name} with config: [{config}]. You can override this with a specific initialization in the derived class.')
        return True

    def cleanup(self):  pass
