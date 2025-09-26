

import importlib


from peripherals.sensors.temperature_switch.config import TempSwitchConfig
from peripherals.sensors.temperature_switch.driver_base import TempSwitchDriverBase
from peripherals.sensors.temperature_switch.simulator import TempSwitchSimulator
from peripherals.sensors.temperature_switch.temp_switch_drivers import TempSwitchDrivers


class TempSwitchFactory:

    @staticmethod
    def create(config:TempSwitchConfig, simulate:bool = False) -> 'TempSwitchDriverBase':

        if (simulate):
            return TempSwitchSimulator(config, True)
        
        driver = config.driver if config.driver is not None else TempSwitchDrivers.Default
        
        class_name = driver.value.upper()
        file_name = driver.value.lower()
        
        module_path = f"peripherals.sensors.temperature_switch.drivers.{file_name}" if not simulate else None

        try:
            module = importlib.import_module(module_path)
            driver_class = getattr(module, class_name)
        except (ModuleNotFoundError, AttributeError) as e:
            raise ImportError(f"Could not load driver '{class_name}': {e}")

        return driver_class(config, False)
       









