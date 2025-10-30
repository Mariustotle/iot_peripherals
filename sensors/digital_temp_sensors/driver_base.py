from abc import abstractmethod
from peripherals.contracts.pins.pin_types import PinType
from peripherals.devices.device_base import DeviceBase
from peripherals.sensors.digital_temp_sensors.config import DigitalTempConfig
from peripherals.sensors.digital_temp_sensors.digital_temp_drivers import DigitalTempDrivers
from peripherals.sensors.sensor import Sensor
from peripherals.sensors.sensor_type import SensorType
from peripherals.sensors.unit_type import UnitType

class DigitalTempDriverBase(Sensor):    
    config:DigitalTempConfig = None
    simulated:bool = None
    gpio_pin:int = None
    
    def __init__(self, config:DigitalTempConfig, device:DeviceBase, simulated:bool = False):
        driver = config.driver if config.driver is not None else DigitalTempDrivers.Default
        driver_name = driver.value if not simulated else 'N/A - Simulated'

        unit_type = UnitType.Celsius if config.measurement == 'Celsius' else UnitType.Fahrenheit

        super().__init__(SensorType.DigitalTemperature, config.name, driver_name, unit_type)
        
        self.config = config
        self.simulated = simulated 
        self.gpio_pin = config.gpio_pin.pin

        if (not self.validate(config)):
            raise Exception(f'Unable to instanciate Digital Temperature Driver [{self.driver_name}] as the config validation failed.')        

    # Can be overrided in driver specific implimentation for special rules
    def validate(self, config:DigitalTempConfig) -> bool:
        return True
        '''
        (validated, reason) = device.validate_pin(PinType.DIGITAL, config.gpio_pin)
        if (not validated):
            print(reason)
        
        return validated
        
        '''
        

