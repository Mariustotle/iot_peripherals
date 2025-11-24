
from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from peripherals.contracts.adapter_type import AdapterType
from peripherals.contracts.pins.pin_config import PinConfig
from peripherals.contracts.pins.pin_details import PinDetails
from peripherals.contracts.pins.pin_position import PinPosition
from peripherals.devices.device_feature import DeviceFeature


class AdapterBase(ABC):
    adapter_type:AdapterType = None
    simulated:bool = None

    @property
    def adapter_name(self) -> str:
        simulator = '' if not self.simulated else f' (Simulated)'
        return f'{self.adapter_type.name}{simulator}'

    def __init__(self, adapter_type:AdapterType, simulated:bool = False):
        self.adapter_type = adapter_type
        self.simulated = simulated


    def validate_i2c(self, name:str, channel:int, i2c_address:int) -> Tuple[List[str], List[str]]:
        debug = []
        errors = []
        
        return (debug, errors)

    def build_i2c_feature(self, instance:int = 0) -> 'DeviceFeature':
        raise Exception(f'Unable to execute _build_i2c_feature for adapter [{self.adapter_name}] #[{instance}] as it is not implimented in the derived class.')

    def build_uart_feature(self, instance:int = 0) -> 'DeviceFeature':
        raise Exception(f'Unable to execute _build_uart_feature for adapter [{self.adapter_name}] #[{instance}] as it is not implimented in the derived class.')

    def build_spi_feature(self, instance:int = 0) -> 'DeviceFeature':
        raise Exception(f'Unable to execute _build_spi_feature for adapter [{self.adapter_name}] #[{instance}] as it is not implimented in the derived class.')

    def build_pwm_feature(self, instance:int = 0) -> 'DeviceFeature':
        raise Exception(f'Unable to execute _build_pwm_feature for adapter [{self.adapter_name}] #[{instance}] as it is not implimented in the derived class.')