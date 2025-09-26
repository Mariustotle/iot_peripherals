

import importlib
from typing import Any

class SensorFactory:

    def __init__(self):
        pass

    @staticmethod
    def create(config:Any, folder_path:str, simulator_class:Any, driver_enum:Any, simulate:bool = False) -> 'Any':

        if (simulate):
            return simulator_class(config, True)
        
        driver = config.driver if config.driver is not None else driver_enum.Default
        
        class_name = driver.value.upper()
        file_name = driver.value.lower()
        
        module_path = f"peripherals.sensors.{folder_path}.drivers.{file_name}" if not simulate else None

        try:
            module = importlib.import_module(module_path)
            driver_class = getattr(module, class_name)
        except (ModuleNotFoundError, AttributeError) as e:
            raise ImportError(f"Could not load driver '{class_name}': {e}")

        return driver_class(config, False)
       









