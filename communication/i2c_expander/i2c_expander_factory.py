

import importlib

from peripherals.communication.i2c_expander.i2c_expander_config import I2CExpanderConfig
from peripherals.communication.i2c_expander.i2c_expander_driver_base import I2CExpanderDriverBase
from peripherals.communication.i2c_expander.i2c_expander_drivers import I2CExpanderDrivers
from peripherals.communication.i2c_expander.simulator import I2CExpanderSimulator


class IOExpanderFactory:

    @staticmethod
    def create(config:I2CExpanderConfig, simulate:bool = False) -> 'I2CExpanderDriverBase':

        if (simulate):
            return I2CExpanderSimulator(config, True)
        
        driver = config.driver if config.driver is not None else I2CExpanderDrivers.Default
        
        class_name = driver.value.upper()
        file_name = driver.value.lower()
        
        module_path = f"peripherals.communication.i2c_expander.drivers.{file_name}" if not simulate else None

        try:
            module = importlib.import_module(module_path)
            driver_class = getattr(module, class_name)
        except (ModuleNotFoundError, AttributeError) as e:
            raise ImportError(f"Could not load driver '{class_name}': {e}")

        return driver_class(config, False)
       









