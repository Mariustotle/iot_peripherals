from abc import abstractmethod


from peripherals.contracts.pins.pin_types import PinType
from peripherals.devices.device_base import DeviceBase
from peripherals.sensors.temperature_switch.config import TempSwitchConfig
from peripherals.sensors.temperature_switch.temp_switch_drivers import TempSwitchDrivers
from peripherals.sensors.sensor import Sensor
from peripherals.sensors.sensor_type import SensorType
from peripherals.sensors.unit_type import UnitType

class TempSwitchDriverBase(Sensor):    
    config:TempSwitchConfig = None
    simulated:bool = None
    gpio_out_pin:int = None
    
    def __init__(self, config:TempSwitchConfig, simulated:bool = False):
        driver = config.driver if config.driver is not None else TempSwitchDrivers.Default
        driver_name = driver.value if not simulated else 'N/A - Simulated'

        unit_type = UnitType.Celsius if config.measurement == 'Celsius' else UnitType.Fahrenheit

        super().__init__(SensorType.TemperatureSwitch, config.name, driver_name, unit_type)
        
        self.config = config
        self.simulated = simulated 
        self.gpio_out_pin = config.gpio_out_pin

        if (not self.validate(config)):
            raise Exception(f'Unable to instanciate Digital Temperature Driver [{self.driver_name}] as the config validation failed.')        

    # Can be overrided in driver specific implimentation for special rules
    def validate(self, config:TempSwitchConfig, device:DeviceBase) -> bool:
        
        (validated, reason) = device.validate_pin(PinType.DIGITAL, config.gpio_out_pin)
        if (not validated):
            print(reason)
        
        return validated

