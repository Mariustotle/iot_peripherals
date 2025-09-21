from abc import ABC, abstractmethod
from common.environment import Env
from peripherals.peripheral_type import PeripheralType


class Peripheral(ABC):   
    peripheral_type: PeripheralType = None
    name: str = None
    
    @property
    def key(self) -> str:
        return f'{self.peripheral_type.value}-{self.name}'
    
    def __init__(self, peripheral_type:PeripheralType, name:str):
        self.peripheral_type = peripheral_type
        self.name = name

    @abstractmethod
    def get_description(self) -> str: pass

    def initialize(self):
        Env.print(f'Default initialization >> {self}')

    def cleanup(self):  pass
