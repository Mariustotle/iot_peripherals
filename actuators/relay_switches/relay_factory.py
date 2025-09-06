

import importlib

from peripherals.actuators.relay_switches.relay_driver import RelayDriver
from peripherals.actuators.relay_switches.relay_driver_base import RelayDriverBase
from peripherals.actuators.relay_switches.relay_config import RelayConfig
from peripherals.actuators.relay_switches.simulator import RelaySimulator


class RelayFactory:

    @staticmethod
    def create(config:RelayConfig, simulate:bool = False) -> 'RelayDriverBase':

        if (simulate):
            return RelaySimulator(config, True)
        
        driver = config.driver if config.driver is not None else RelayDriver.Default
        
        class_name = driver.value.upper()
        namespace_name = driver.value.lower()
        
        module_path = f"peripherals.actuators.relay_switches.{namespace_name}.driver" if not simulate else None

        try:
            module = importlib.import_module(module_path)
            driver_class = getattr(module, class_name)
        except (ModuleNotFoundError, AttributeError) as e:
            raise ImportError(f"Could not load driver '{namespace_name}': {e}")

        return driver_class(config, False)
       









