
from enum import Enum
import importlib

from peripherals.actuators.relay_switches.relay_driver_base import RelayDriverBase
from peripherals.actuators.relay_switches.jqc3f_05vdc_c.driver import JQC3F_05VDC_C
from peripherals.actuators.relay_switches.relay_config import RelayConfig
from peripherals.actuators.relay_switches.simulator import RelaySimulator

class RelayDevice(Enum):
    Default = 'jqc3f_05vdc_c'
    JQC3F_05VDC_C = 'jqc3f_05vdc_c'             # Two state relay switch with LED status lights

class RelayFactory:

    @staticmethod
    def create(config:RelayConfig, device: RelayDevice = RelayDevice.Default, simulate:bool = False) -> 'RelayDriverBase':

        if (simulate):
            return RelaySimulator('Simulator', config, True)
        
        driver_name = device.value
        module_path = f"peripherals.actuators.relay_switches.{driver_name}.driver"
        class_name = driver_name.upper()

        try:
            module = importlib.import_module(module_path)
            driver_class = getattr(module, class_name)
        except (ModuleNotFoundError, AttributeError) as e:
            raise ImportError(f"Could not load driver '{driver_name}': {e}")

        return driver_class(device, config, False)
       









