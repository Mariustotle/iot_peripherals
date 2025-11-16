from abc import ABC, abstractmethod
import importlib
from typing import Any

from peripherals.factory_mapping import FactoryMapping
from peripherals.peripheral_type import PeripheralType

class PeripheralFactory(ABC):
    folder_path: str = None
    peripherl_type: str = None    

    def __init__(self, folder_path:str, peripheral_type:PeripheralType):
        self.folder_path = folder_path
        self.peripherl_type = peripheral_type

    @abstractmethod
    def get_details(self, config:Any) -> 'FactoryMapping': pass

    def create(self, config:Any, simulate:bool = False) -> 'Any':
        
        details = self.get_details(config)
        driver = config.driver if config.driver is not None else details.driver_enum.Default
        
        class_name = driver.value.upper()
        driver_name = driver.value.lower()

        pin_layout_class = self.get_pin_layout_class('PinLayout', driver_name, details.peripheral_path)

        if (simulate):
            actual_driver_pins = pin_layout_class.get_pin_layout()
            return details.simulator_class(config, actual_driver_pins)
        
        driver_class = self.get_driver_class(class_name, driver_name, details.peripheral_path)
        
        return driver_class(config, False, )


    def get_driver_class(self, class_name:str, driver_name:str, peripheral_path:str):
        
        try:
            module_path = f"peripherals.{self.folder_path}.{peripheral_path}.drivers.{driver_name}.driver"
            module = importlib.import_module(module_path)
            driver_class = getattr(module, class_name)

            return driver_class

        except (ModuleNotFoundError, AttributeError) as e:
            raise ImportError(f"Could not load driver '{class_name}' Path [{module_path}]: {e}")

       
    def get_pin_layout_class(self, class_name:str, driver_name:str, peripheral_path:str):
        
        try:
            module_path = f"peripherals.{self.folder_path}.{peripheral_path}.drivers.{driver_name}.pin_layout"
            module = importlib.import_module(module_path)
            driver_class = getattr(module, class_name)

            return driver_class

        except (ModuleNotFoundError, AttributeError) as e:
            raise ImportError(f"Could not load driver '{class_name}' Path [{module_path}]: {e}")
