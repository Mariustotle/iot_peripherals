from abc import abstractmethod
from typing import Optional, Dict
from peripherals.contracts.pins.pin_details import PinDetails
from peripherals.contracts.pins.pin_position import PinPosition
from peripherals.devices.device_base import DeviceBase
from peripherals.sensors.sensor import Sensor
from peripherals.sensors.sensor_type import SensorType
from peripherals.sensors.tds_sensors.config import TDSConfig
from peripherals.sensors.tds_sensors.tds_drivers import TDSDrivers

from peripherals.sensors.unit_type import UnitType

import time

class TDSDriverBase(Sensor):
    config:TDSConfig = None
    
    def __init__(self, config:TDSConfig, simulated:bool = False, pins:Optional[Dict[PinPosition, PinDetails]] = None):
        driver = config.driver if config.driver is not None else TDSDrivers.Default

        super().__init__(simulated, SensorType.TDS, config.name, driver.value, unit_type=UnitType.TDS, config=config, pins=pins)

        if (not self.validate(config)):
            raise Exception(f'Unable to instanciate communication driver [{self.driver_name}] as the config validation failed.')        


    def read_multiple(self, number_of_reads:int) -> float:
        total = 0.0

        for take in range (0, number_of_reads):
            total += self.read_once()

            if (take < number_of_reads and self.config.delay_between_readings > 0):
                time.sleep(self.config.delay_between_readings)

        average = total / number_of_reads

        return average

    @abstractmethod
    def read_once(self) -> float: pass
    
    def _default_reading(self) -> float:        
        if (self.config.number_of_readings is None or self.config.number_of_readings < 1):
            reading = self.read_once()
            return reading
        
        average = self.read_multiple(self.config.number_of_readings)    
        return average


    def get_description(self) -> str: 
        return f"Peripheral: [{self.peripheral_type.name}], Communication: [{self.sensor_type.name}], Driver: [{self.driver_name}] over average of [{self.config.number_of_readings}] readings."

    # Can be overrided in driver specific implimentation for special rules
    def validate(self, config:TDSConfig) -> bool: return True
        
