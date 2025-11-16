from typing import Optional, Dict

from peripherals.contracts.pins.pin_details import PinDetails
from peripherals.contracts.pins.pin_position import PinPosition
from peripherals.sensors.temperature_switch.config import TempSwitchConfig
from peripherals.sensors.temperature_switch.temp_switch_drivers import TempSwitchDrivers
from peripherals.sensors.sensor import Sensor
from peripherals.sensors.sensor_type import SensorType
from peripherals.sensors.unit_type import UnitType

class TempSwitchDriverBase(Sensor):    
    config:TempSwitchConfig = None
    gpio_out_pin:int = None
    
    def __init__(self, config:TempSwitchConfig, simulated:bool = False, pins:Optional[Dict[PinPosition, PinDetails]] = None):
        driver = config.driver if config.driver is not None else TempSwitchDrivers.Default
        unit_type = UnitType.Celsius if config.measurement == 'Celsius' else UnitType.Fahrenheit

        super().__init__(simulated, SensorType.TemperatureSwitch, config.name, driver.value, unit_type, config=config, pins=pins)
        
        self.gpio_out_pin = config.gpio_out_pin

        if (not self.validate(config)):
            raise Exception(f'Unable to instanciate Digital Temperature Driver [{self.driver_name}] as the config validation failed.')        

    # Can be overrided in driver specific implimentation for special rules
    def validate(self, config:TempSwitchConfig) -> bool:
        return True
    
        '''
        (validated, reason) = device.validate_pin(PinType.DIGITAL, config.gpio_out_pin)
        if (not validated):
            print(reason)
        
        return validated
        '''
        

