from abc import abstractmethod

import time

from peripherals.sensors.sensor import Sensor
from peripherals.sensors.sensor_reading import SensorReading
from peripherals.sensors.sensor_type import SensorType
from peripherals.sensors.tds_sensors.tds_config import TDSConfig
from peripherals.sensors.tds_sensors.tds_drivers import TDSDrivers
from peripherals.sensors.read_decorator import read
from datetime import datetime


class TDSDriverBase(Sensor):
    config:TDSConfig = None
    simulated:bool = None
    
    def __init__(self, config:TDSConfig, simulated:bool = False):
        driver = config.driver if config.driver is not None else TDSDrivers.Default
        driver_name = driver.value if not simulated else 'N/A - Simulated'

        super().__init__(SensorType.TDS, config.name, driver_name)
        
        self.config = config
        self.simulated = simulated 

        if (not self.validate(config)):
            raise Exception(f'Unable to instanciate communication driver [{self.driver_name}] as the config validation failed.')        

    # Can be overrided in driver specific implimentation for special rules
    def validate(self, config:TDSConfig) -> bool:  return True

    def read_multiple(self, number_of_reads:int) -> float:
        total = 0.0

        for take in range (0, number_of_reads):
            total += self.read_once()

            if (take < number_of_reads and self.config.delay_between_readings > 0):
                time.sleep(self.config.delay_between_readings)

        average = total / number_of_reads

        return SensorReading.create(average, self)

    @abstractmethod
    def read_once(self) -> float: pass
    
    def _default_reading(self) -> SensorReading[float]:
        
        if (self.config.number_of_readings is None or self.config.number_of_readings < 1):
            reading = self.read_once()
            return SensorReading.create(reading, self)
        
        reading = self.read_multiple(self.config.number_of_readings)
        response = SensorReading.create(reading, self)

        self.read_time = response.read_time        
        return response


    def get_description(self) -> str: 
        return f"Peripheral: [{self.peripheral_type.name}], Communication: [{self.sensor_type.name}], Driver: [{self.driver_name}] over average of [{self.config.number_of_readings}] readings."




