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

        if (simulate):
            return details.simulator_class(config, True)
        
        driver = config.driver if config.driver is not None else details.driver_enum.Default
        
        class_name = driver.value.upper()
        file_name = driver.value.lower()
        
        return self.create_driver_instance(config, file_name, class_name, details.peripheral_path)


    def create_driver_instance(self, config:Any, file_name:str, class_name:str, peripheral_path:str) -> 'Any':      
        module_path = f"peripherals.{self.folder_path}.{peripheral_path}.drivers.{file_name}"

        try:
            module = importlib.import_module(module_path)
            driver_class = getattr(module, class_name)

        except (ModuleNotFoundError, AttributeError) as e:
            raise ImportError(f"Could not load driver '{class_name}' Path [{module_path}]: {e}")

        return driver_class(config, False)
       
