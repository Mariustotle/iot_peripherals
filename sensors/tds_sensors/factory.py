

import importlib

from peripherals.sensors.tds_sensors.tds_drivers import TDSDrivers
from peripherals.sensors.tds_sensors.config import TDSConfig
from peripherals.sensors.tds_sensors.driver_base import TDSDriverBase
from peripherals.sensors.tds_sensors.simulator import TDSSimulator


class TDSFactory:

    @staticmethod
    def create(config:TDSConfig, simulate:bool = False) -> 'TDSDriverBase':

        if (simulate):
            return TDSSimulator(config, True)
        
        driver = config.driver if config.driver is not None else TDSDrivers.Default
        
        class_name = driver.value.upper()
        file_name = driver.value.lower()
        
        module_path = f"peripherals.sensors.tds_sensors.drivers.{file_name}" if not simulate else None

        try:
            module = importlib.import_module(module_path)
            driver_class = getattr(module, class_name)
        except (ModuleNotFoundError, AttributeError) as e:
            raise ImportError(f"Could not load driver '{class_name}': {e}")

        return driver_class(config, False)
       









