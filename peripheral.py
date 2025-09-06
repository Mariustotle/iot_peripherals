from abc import ABC, abstractmethod
from peripherals.peripheral_type import PeripheralType


class Peripheral(ABC):   
    peripheral_type: PeripheralType = None
    device_name: str = None
    
    @property
    def key(self) -> str:
        return f'{self.peripheral_type.value}-{self.device_name}'
    
    def __init__(self, peripheral_type:PeripheralType, device_name:str):
        self.peripheral_type = peripheral_type
        self.device_name = device_name

    @abstractmethod
    def get_description(self) -> str: pass
