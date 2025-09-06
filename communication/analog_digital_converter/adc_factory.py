

import importlib

from peripherals.actuators.relay_switches.relay_drivers import RelayDrivers
from peripherals.communication.analog_digital_converter.adc_driver_base import ADCDriverBase
from peripherals.communication.analog_digital_converter.simulator import ADCSimulator
from peripherals.communication.analog_digital_converter.adc_config import ADCConfig


class ADCFactory:

    @staticmethod
    def create(config:ADCConfig, simulate:bool = False) -> 'ADCDriverBase':

        if (simulate):
            return ADCSimulator(config, True)
        
        driver = config.driver if config.driver is not None else RelayDrivers.Default
        
        class_name = driver.value.upper()
        file_name = driver.value.lower()
        
        module_path = f"peripherals.commmunication.analog_digital_converter.drivers.{file_name}" if not simulate else None

        try:
            module = importlib.import_module(module_path)
            driver_class = getattr(module, class_name)
        except (ModuleNotFoundError, AttributeError) as e:
            raise ImportError(f"Could not load driver '{class_name}': {e}")

        return driver_class(config, False)
       









