from peripherals.devices.device_base import DeviceBase
from peripherals.sensors.temperature_sensors.config.temperature_base_config import TemperatureBaseConfig
from peripherals.sensors.temperature_sensors.temperature_drivers import TemperatureDrivers
from peripherals.sensors.sensor import Sensor
from peripherals.sensors.sensor_type import SensorType
from peripherals.sensors.unit_type import UnitType

class TemperatureDriverBase(Sensor):    
    config:TemperatureBaseConfig = None
    simulated:bool = None
    
    def __init__(self, config:TemperatureBaseConfig, device:DeviceBase, simulated:bool = False):
        driver = config.driver if config.driver is not None else TemperatureDrivers.Default
        driver_name = driver.value if not simulated else 'N/A - Simulated'

        unit_type = UnitType.Celsius if config.measurement == 'Celsius' else UnitType.Fahrenheit

        super().__init__(SensorType.DigitalTemperature, config.name, driver_name, unit_type)
        
        self.config = config
        self.simulated = simulated 

        if (not self.validate(config)):
            raise Exception(f'Unable to instanciate Digital Temperature Driver [{self.driver_name}] as the config validation failed.')        

    # Can be overrided in driver specific implimentation for special rules
    def validate(self, config:TemperatureBaseConfig) -> bool:
        return True
        '''
        (validated, reason) = device.validate_pin(PinType.DIGITAL, config.gpio_pin)
        if (not validated):
            print(reason)
        
        return validated
        
        '''
        

