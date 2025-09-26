

import importlib


from peripherals.sensors.digital_temp_sensors.config import DigitalTempConfig
from peripherals.sensors.digital_temp_sensors.driver_base import DigitalTempDriverBase
from peripherals.sensors.digital_temp_sensors.simulator import DigitalTempSimulator
from peripherals.sensors.digital_temp_sensors.temperature_drivers import DigitalTempDrivers


class DigitalTempFactory:

    @staticmethod
    def create(config:DigitalTempConfig, simulate:bool = False) -> 'DigitalTempDriverBase':

        if (simulate):
            return DigitalTempSimulator(config, True)
        
        driver = config.driver if config.driver is not None else DigitalTempDrivers.Default
        
        class_name = driver.value.upper()
        file_name = driver.value.lower()
        
        module_path = f"peripherals.sensors.digital_temp_sensors.drivers.{file_name}" if not simulate else None

        try:
            module = importlib.import_module(module_path)
            driver_class = getattr(module, class_name)
        except (ModuleNotFoundError, AttributeError) as e:
            raise ImportError(f"Could not load driver '{class_name}': {e}")

        return driver_class(config, False)
       









