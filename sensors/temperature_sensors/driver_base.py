from typing import Dict, Optional
from peripherals.contracts.pins.pin_details import PinDetails
from peripherals.contracts.pins.pin_position import PinPosition
from peripherals.devices.device_base import DeviceBase
from peripherals.sensors.temperature_sensors.config.temperature_base_config import TemperatureBaseConfig
from peripherals.sensors.temperature_sensors.temperature_drivers import TemperatureDrivers
from peripherals.sensors.sensor import Sensor
from peripherals.sensors.sensor_type import SensorType
from peripherals.sensors.unit_type import UnitType

class TemperatureDriverBase(Sensor):    
    config:TemperatureBaseConfig = None
    
    def __init__(self, config:TemperatureBaseConfig, simulated:bool = False, pins:Optional[Dict[PinPosition, PinDetails]] = None):
        driver = config.driver if config.driver is not None else TemperatureDrivers.Default
        unit_type = UnitType.Celsius if config.measurement == 'Celsius' else UnitType.Fahrenheit

        super().__init__(simulated, SensorType.DigitalTemperature, config.name, driver.value, unit_type, config=config, pins=pins)

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
        

