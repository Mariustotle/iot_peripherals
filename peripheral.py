from abc import abstractmethod
from typing import Optional
from common.environment import Env
from peripherals.contracts.board.board_base import BoardBase
from peripherals.peripheral_type import PeripheralType

class Peripheral(BoardBase):
    peripheral_type: PeripheralType = None
    
    @property
    def key(self) -> str:
        return f'{self.peripheral_type.value}-{self.name}'
    
    def __init__(self, peripheral_type:PeripheralType, name:str, parent:Optional['BoardBase'] = None):
        self.peripheral_type = peripheral_type
        super().__init__(name=name, parent=parent)

    @abstractmethod
    def get_description(self) -> str: pass

    def initialize(self) -> bool:
        Env.print(f'Default initialization >> {self}')
        return True

    def cleanup(self):  pass
