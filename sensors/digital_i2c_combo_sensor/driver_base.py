from abc import abstractmethod

from peripherals.devices.device_base import DeviceBase
from peripherals.sensors.digital_i2c_combo_sensor.config import DigitalComboConfig
from peripherals.sensors.digital_i2c_combo_sensor.digital_combo_drivers import DigitalComboDrivers
from peripherals.sensors.sensor import Sensor
from peripherals.sensors.sensor_type import SensorType

class DigitalComboDriverBase(Sensor):    
    config:DigitalComboConfig = None
    simulated:bool = None
    gpio_pin:int = None
    
    def __init__(self, config:DigitalComboConfig, simulated:bool = False):
        driver = config.driver if config.driver is not None else DigitalComboDrivers.Default
        driver_name = driver.value if not simulated else 'N/A - Simulated'

        # No Single Unit
        super().__init__(SensorType.DigitalTemperature, config.name, driver_name, unit_type = None)
        
        self.config = config
        self.simulated = simulated 

        if (not self.validate(config)):
            raise Exception(f'Unable to instanciate Digital Temperature Driver [{self.driver_name}] as the config validation failed.')        

    # Can be overrided in driver specific implimentation for special rules
    def validate(self, config:DigitalComboConfig) -> bool:
        
        # How to validate features?
        
        return True
