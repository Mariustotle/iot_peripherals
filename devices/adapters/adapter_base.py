
from abc import ABC, abstractmethod
from typing import List, Optional

from peripherals.contracts.adapter_type import AdapterType
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

    def build_i2c_feature(self, name:Optional[str] = None) -> 'DeviceFeature':
        raise Exception(f'Unable to execute _build_i2c_feature for adapter [{self.adapter_name}] as it is not implimented in the derived class.')

    def build_uart_feature(self, name:Optional[str] = None) -> 'DeviceFeature':
        raise Exception(f'Unable to execute _build_uart_feature for adapter [{self.adapter_name}] as it is not implimented in the derived class.')

    def build_spi_feature(self, name:Optional[str] = None) -> 'DeviceFeature':
        raise Exception(f'Unable to execute _build_spi_feature for adapter [{self.adapter_name}] as it is not implimented in the derived class.')

    def build_pwm_feature(self, name:Optional[str] = None) -> 'DeviceFeature':
        raise Exception(f'Unable to execute _build_pwm_feature for adapter [{self.adapter_name}] as it is not implimented in the derived class.')